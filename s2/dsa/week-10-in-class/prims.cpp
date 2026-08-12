#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <algorithm>

using namespace std;

// Structure to represent an edge
struct Edge {
    int src, dest, weight;
    Edge(int s, int d, int w) : src(s), dest(d), weight(w) {}
};

// Comparator for priority queue
struct CompareEdge {
    bool operator()(const Edge& e1, const Edge& e2) {
        return e1.weight > e2.weight;
    }
};

// Class to represent a graph
class Graph {
private:
    int V;
    vector<vector<pair<int, int>>> adjList; // Adjacency list representation

public:
    Graph(int vertices) : V(vertices) {
        adjList.resize(V);
    }

    // Function to add an edge to the graph
    void addEdge(int src, int dest, int weight) {
        adjList[src].push_back(make_pair(dest, weight));
        adjList[dest].push_back(make_pair(src, weight)); // Graph is undirected
    }

    // Function to perform Prim's algorithm to find MST
    vector<Edge> primMST(int startNode) {
        // Priority queue to store edges
        priority_queue<Edge, vector<Edge>, CompareEdge> pq;
        vector<bool> inMST(V, false); // To track vertices already in MST
        vector<Edge> mstEdges; // To store the edges of MST

        // Add starting node to MST
        inMST[startNode] = true;

        // Add all edges connected to starting node to priority queue
        for (auto neighbor : adjList[startNode]) {
            // <----- ADD YOUR CODE HERE ----->
            Edge edge = Edge(startNode, neighbor.first, neighbor.second);
            pq.push(edge);
        
        }

        while (!pq.empty()) {
            Edge e = pq.top(); // Get the minimum weight edge
            pq.pop();

            int u = e.dest;

            // If destination is already in MST, skip this edge
            // <----- ADD YOUR CODE HERE ----->
            if (inMST[u]) continue;

            // Add edge to MST
            // <----- ADD YOUR CODE HERE ----->
            mstEdges.push_back(e);
            inMST[u] = true;

            // Add all edges connected to u to priority queue
            // <----- ADD YOUR CODE HERE ----->
            for (auto neighbor : adjList[u]) {
                int v = neighbor.first;
                int weight = neighbor.second;
                if (!inMST[v]) {
                    Edge edge = Edge(u, v, weight);
                    pq.push(edge);
                }
            }
        }

        return mstEdges;
    }

    // Function to print edges of MST ordered by minimum of edge.src and edge.dest
    void printMST(vector<Edge>& mstEdges) {
        sort(mstEdges.begin(), mstEdges.end(), [](const Edge& e1, const Edge& e2) {
            int min1 = min(e1.src, e1.dest);
            int min2 = min(e2.src, e2.dest);
            return min1 < min2 || (min1 == min2 && e1.src + e1.dest < e2.src + e2.dest);
        });
    
        for (const auto& edge : mstEdges) {
            cout << "(" << min(edge.src, edge.dest) << ", " << max(edge.src, edge.dest) << ") - Weight: " << edge.weight << endl;
        }
    }

};

int main() {
    // Create a graph
    Graph g(6);

    // Add edges to the graph
    g.addEdge(0, 1, 3);
    g.addEdge(0, 5, 1);
    g.addEdge(1, 2, 2);
    g.addEdge(1, 3, 1);
    g.addEdge(1, 4, 10);
    g.addEdge(2, 3, 3);
    g.addEdge(2, 5, 5);
    g.addEdge(3, 4, 5);
    g.addEdge(4, 5, 4);

    int startNode; // Starting node for Prim's algorithm
    cin >> startNode;

    // Find minimum spanning tree using Prim's algorithm
    vector<Edge> mstEdges = g.primMST(startNode);

    // Print the edges of MST
    g.printMST(mstEdges);

    return 0;
}
