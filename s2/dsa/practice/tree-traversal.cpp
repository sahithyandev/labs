#include "iostream" 
#include <queue>

using namespace std;

class Node {
    public:
        int value;
        Node* left = NULL;
        Node* right = NULL;
        Node(int value): value(value) {}
        
        void postOrderTraversal() {
            if (this->left != NULL) {
                this->left->postOrderTraversal();
            }
            if (this->right != NULL) {
                this->right->postOrderTraversal();
            }
            cout << this->value << " ";
        }
        void preOrderTraversal() {
            cout << this->value << " ";
            if (this->left != NULL) {
                this->left->preOrderTraversal();
            }
            if (this->right != NULL) {
                this->right->preOrderTraversal();
            }
        }
        void inOrderTraversal() {
            if (this->left != NULL) {
                this->left->inOrderTraversal();
            }
            cout << this->value << " ";
            if (this->right != NULL) {
                this->right->inOrderTraversal();
            }
        }
        void levelOrderTraversal() {
            queue<Node*> q;
            q.push(this);
            
            while (!q.empty()) {
                Node* top = q.front();
                q.pop();
                
                if (top->left != NULL) {
                    q.push(top->left);
                }
                if (top->right != NULL) {
                    q.push(top->right);
                }
                cout << top->value << " "; 
            }
        }
};

int main() {
    Node* node1 = new Node(1);
    Node* node2 = new Node(2);
    Node* node3 = new Node(3);
    Node* node4 = new Node(4);
    Node* node5 = new Node(5);
    Node* node6 = new Node(6);
    Node* node7 = new Node(7);
    Node* node8 = new Node(8);
    Node* node9 = new Node(9);
    
    // The below tree is expressed here.
    //        1   
    //     2      3
    //   4   6  5   7
    // 8   9
    
    node1->left = node2;
    node1->right = node3;
    node2->left = node4;
    node2->right = node6;
    node3->left = node5;
    node3->right = node7;
    node4->left = node8;
    node4->right = node9;
    
    cout << "POST ORDER: ";
    node1->postOrderTraversal();
    cout << "\n";
    
    cout << "PRE ORDER: ";
    node1->preOrderTraversal();
    cout << "\n";
    
    cout << "IN ORDER: ";
    node1->inOrderTraversal();
    cout << "\n";
    
    cout << "LEVEL ORDER: ";
    node1->levelOrderTraversal();
    cout << "\n";
    
    return 0;
}
