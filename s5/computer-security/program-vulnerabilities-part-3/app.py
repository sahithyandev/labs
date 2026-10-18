#!/usr/bin/env python3

# SQL injection demo (Python standard library only, no installs)
#
# RUN:  python3 app.py   then open http://localhost:8000
#
# DATABASE: nothing to set up. init_db() auto-creates the SQLite file shop.db
# on start-up. Equivalent SQL (delete shop.db to reset):
#   CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT,
#                          public INTEGER);  -- 0 = hidden from searches
#   INSERT INTO products (name, public) VALUES ('apple',1), ('banana',1),
#          ('cherry',1), ('SECRET: staff discount code 1234',0);
#
# ATTACK: search "x' OR 1=1 --". The vulnerable button also returns the hidden
# SECRET row; the secure button returns nothing.
 
import html
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

DB = "shop.db"


def init_db():
    # Create and seed the table on first run.
    with sqlite3.connect(DB) as db:
        db.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY,"
                   " name TEXT, public INTEGER)")
        if not db.execute("SELECT 1 FROM products").fetchone():
            db.executemany("INSERT INTO products (name, public) VALUES (?, ?)",
                           [("apple", 1), ("banana", 1), ("cherry", 1),
                            ("EXCLUSIVE PRODUCT NOT RELEASED YET (SECRET)", 0)])


# ------------------------- PART 1: VULNERABLE CODE ---------------------------
def search_vulnerable(term):
    # VULNERABLE: input is concatenated into the SQL text. "x' OR 1=1 --"
    # matches every row and "--" comments out "public = 1", leaking hidden rows.
    query = f"SELECT name FROM products WHERE name LIKE '%{term}%' AND public = 1"
    with sqlite3.connect(DB) as db:
        return db.execute(query).fetchall(), query


# --------------------------- PART 2: SECURE CODE -----------------------------
def search_secure(term):
    # SAFE: parameterised query. The "?" value is passed as data, never as SQL.
    query = "SELECT name FROM products WHERE name LIKE ? AND public = 1"
    with sqlite3.connect(DB) as db:
        return db.execute(query, (f"%{term}%",)).fetchall(), query


# ------------------------------ WEB INTERFACE --------------------------------
PAGE = """<h2>SQL injection demo: product search</h2>
<p>The search is meant to return only <b>public</b> products. The database also
holds one hidden product that no search should ever show.</p>
<ol>
<li>Search for <code>an</code> with either button: only "banana" is returned
(normal use).</li>
<li>Search for <code>x' OR 1=1 --</code> with <b>Search (vulnerable)</b>: all
products are returned, including the hidden SECRET one. The input was pasted
into the SQL text, so <code>OR 1=1</code> matches every row and <code>--</code>
comments out the <code>public = 1</code> check.</li>
<li>Search for the same text with <b>Search (secure)</b>: no results. The
parameterised query treats the input as plain data, never as SQL.</li>
<li>Search for a single <code>'</code> with the vulnerable button: an SQL syntax
error appears, which shows the input is reaching the SQL parser.</li>
</ol>
<p>The executed SQL is printed under the form so you can compare both queries.</p>
<form>
<input name=q value="{q}">
<button formaction=/vulnerable>Search (vulnerable)</button>
<button formaction=/secure>Search (secure)</button>
</form>
<pre>{query}</pre>
<ul>{rows}</ul>"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        q = parse_qs(url.query).get("q", [""])[0]
        query, rows = "", []
        if url.path in ("/vulnerable", "/secure"):
            search = search_vulnerable if url.path == "/vulnerable" else search_secure
            try:
                found, query = search(q)
                rows = [r[0] for r in found] or ["(no results)"]
            except sqlite3.Error as e:
                # Shown so the SQL error caused by injected input is visible.
                rows = [f"SQL error: {e}"]
        # Escape everything echoed back so this demo adds no XSS of its own.
        body = PAGE.format(q=html.escape(q, quote=True), query=html.escape(query),
                           rows="".join(f"<li>{html.escape(r)}</li>" for r in rows))
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(body.encode())


if __name__ == "__main__":
    init_db()
    print("Open http://localhost:8000")
    HTTPServer(("localhost", 8000), Handler).serve_forever()
