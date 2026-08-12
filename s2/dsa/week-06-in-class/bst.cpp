#include <iostream>
using namespace std;

struct node
{
	int key;
	struct node *left, *right;
};

// Inorder traversal
void traverseInOrder(struct node *root)
{
	if (!root)
	{
		return;
	}
	traverseInOrder(root->left);
	cout << root->key << " ";
	traverseInOrder(root->right);
}

// Insert a node
struct node *insertNode(struct node *node, int key)
{
	if (node == NULL)
	{
		node = new struct node;
		node->key = key;
		node->left = NULL;
		node->right = NULL;
		return node;
	}

	if (node->key > key)
	{
		node->left = insertNode(node->left, key);
	}
	else
	{
		node->right = insertNode(node->right, key);
	}

	return node;
}

// Deleting a node
struct node *deleteNode(struct node *root, int key)
{
	if (root == NULL)
	{
		return root;
	}

	if (root->key > key)
	{
		root->left = deleteNode(root->left, key);
	}

	else if (root->key < key)
	{
		root->right = deleteNode(root->right, key);
	}
	// Otherwise root key is the node to be deleted
	else
	{
		// Case 1: Node has no childs
		if (root->left == NULL && root->right == NULL)
		{
			delete root;
			root = NULL;
			return root;
		}
		// Case 2: Node has right child only
		if (!root->left)
		{
			struct node *temp = root;
			root = temp->right;
			delete temp;
			return root;
		}
		// Case 3: Node has left child only
		if (!root->right)
		{
			struct node *temp = root;
			root = temp->left;
			delete temp;
			return root;
		}

		// Case 4: Node has two children
		// get the smallest in the right subtree
		struct node *temp = root->right;
		while (temp->left)
		{
			temp = temp->left;
		}
		root->key = temp->key;
		root->right = deleteNode(root->right, temp->key);
	}
	return root;
}

// Driver code
int main()
{
	struct node *root = NULL;

	int operation;
	int operand;
	cin >> operation;

	while (operation != -1)
	{
		switch (operation)
		{
		case 1: // insert
			cin >> operand;
			root = insertNode(root, operand);
			cout << "Inserted " << operand << endl;
			cin >> operation;
			break;
		case 2: // delete
			cin >> operand;
			root = deleteNode(root, operand);
			cout << "Deleted " << operand << endl;
			cin >> operation;
			break;
		case 3: // travers
			traverseInOrder(root);
			cout << "\n";
			cin >> operation;
			break;
		default:
			cout << "Invalid Operator!\n";
			return 0;
		}
	}

	traverseInOrder(root);
}