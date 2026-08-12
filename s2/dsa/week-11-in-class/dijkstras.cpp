
#include <iostream>
#include <vector>
#include <limits>

#define INF numeric_limits<int>::max()

using namespace std;

// Function to find the vertex with minimum distance value,
// from the set of vertices not yet included in shortest path tree
int minDistance(const vector<int>& dist, const vector<bool>& visited, int V) {
    int minDist = INF, minIndex = -1;

    // <--- TODO: Find the unvisited vertex with the minimum distance
    for (int i = 0; i < V; i++) {
        if (visited[i] || dist[i] >= minDist) continue;
        
        minDist = dist[i];
        minIndex = i;
    }
    
    return minIndex;
}

// Dijkstra's algorithm for single source shortest path
vector<int> dijkstra(const vector<vector<int>>& graph, int src) {
    int V = graph.size();
    vector<int> dist(V, INF); // Initialize distances as infinite
    vector<bool> visited(V, false); // Mark all vertices as not visited

    dist[src] = 0; // Distance of source vertex from itself is always 0

    // Find shortest path for all vertices
    for (int count = 0; count < V - 1; ++count) {
        // <--- TODO: Pick the minimum distance vertex from the set of vertices not yet processed --->
        int u = minDistance(dist, visited, V);
        
        if (u == -1) {
            // If no unvisited vertex with a finite distance is found, the algorithm terminates
            break;
        }
        
        // <--- TODO: Mark the picked vertex as processed --->
        visited[u] = true;

        // Update dist value of the adjacent vertices of the picked vertex
        for (int v = 0; v < V; ++v) {
            // <--- TODO: Update dist[v] only if:
            // - it is not in the visited set
            // - there is an edge from u to v
            // - total weight of path from src to v through u is smaller than current value of dist[v]
            // --->
            if (visited[v] || graph[u][v] == INF) {
                continue;
            }
            
            int distance_through_u = dist[u] + graph[u][v];
            
            if (distance_through_u < dist[v]) {
                dist[v] = distance_through_u;
            }
        }
    }

    // Return the shortest distance from src to dest
    return dist;
}

// Function to print shortest distances from source node to all other nodes
void printShortestDistances(const vector<int>& dist) {
    int V = dist.size();
    for (int i = 0; i < V; ++i) {
        cout << "Node " << i << ": " << dist[i] << endl;
    }
}

int main() {
    // <--- TODO: Update the following graph with the correct weighted adjacency matrix --->
    vector<vector<int>> graph = {
        {INF, 10, INF, INF, 15, 5},
        {10, INF, 10, 30, INF, INF},
        {INF, 10, INF, 12, 5, INF},
        {INF, 30, 12, INF, INF, 20},
        {15, INF, 5, INF, INF, INF},
        {5, INF, INF, 20, INF, INF},
    };
    
    int src;
    cin >> src;

    vector<int> dist = dijkstra(graph, src);
    printShortestDistances(dist);

    return 0;
}
