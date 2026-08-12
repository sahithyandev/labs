#include <iostream>
#include <queue>
#include <stack>
#include <vector>
using namespace std;

struct Node
{
    int label;
    vector<int> neighbours;
};

struct Graph
{
    int n = 8;
    Node *nodes = new Node[n];

    void intializeNodes()
    {
        for (int i = 0; i < n; i++)
        {
            nodes[i].label = i + 1;
        }
    }

    void addEdge(int u, int v)
    {
        nodes[u - 1].neighbours.push_back(v);
        nodes[v - 1].neighbours.push_back(u);
    }

    void print()
    {
        // Iterate through each node and print its neighbours
        for (int i = 0; i < n; i++)
        {
            cout << nodes[i].label << "-->";
            for (auto nd : nodes[i].neighbours)
            {
                cout << nd << " ";
            }
            cout << "\n";
        }
    }
    
    void depthFirstTraversal(Node& start) {
        vector<bool> visited(n, false);
        stack<Node*> discoveredNodes;
        
        discoveredNodes.push(&start);
        
        while (!discoveredNodes.empty()) {
            Node* current = discoveredNodes.top();
            discoveredNodes.pop();
            
            if (visited[current->label - 1]) continue;
            visited[current->label - 1] = true;
            cout << current->label << " ";
            
            for (auto nb : current->neighbours) {
                Node *n = &this->nodes[nb - 1];
                if (visited[nb - 1]) continue;
                discoveredNodes.push(n);
            }
        }
        cout << endl;
    }
    void breadthFirstTraversal(Node& start) {
        vector<bool> visited(n, false);
        queue<Node*> discoveredNodes;
        discoveredNodes.push(&start);
        
        while (!discoveredNodes.empty()) {
            Node* current = discoveredNodes.front();
            discoveredNodes.pop();
            
            if (visited[current->label - 1]) continue;
            visited[current->label - 1] = true;
            cout << current->label << " ";
            
            for (auto nb : current->neighbours) {
                Node *n = &this->nodes[nb - 1];
                if (visited[nb - 1]) continue;
                discoveredNodes.push(n);
            }
        }
        cout << endl;
    }
    ~Graph() {
        delete[] nodes;
    }
};

int main()
{
    Graph *g = new Graph;
    g->intializeNodes();
    
    g->addEdge(1, 2);
    g->addEdge(1, 3);
    g->addEdge(1, 5);
    g->addEdge(1, 4);

    g->addEdge(2, 3);
    g->addEdge(2, 6);

    g->addEdge(4, 6);
    g->addEdge(4, 7);
    g->addEdge(4, 8);

    g->addEdge(5, 6);
    g->addEdge(5, 7);
    g->addEdge(5, 8);

    g->breadthFirstTraversal(g->nodes[0]);
    return 0;
}
