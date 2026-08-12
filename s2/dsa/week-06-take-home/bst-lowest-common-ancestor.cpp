#include <iostream>
#include <vector>

using namespace std;

/**
 * @brief Reads a specified number of integers from standard input and returns them as a vector.
 *
 * This function prompts the user to input a series of integers. It reads the integers one by one
 * until the specified length is reached or a non-space character is encountered in the input stream.
 *
 * @param length The number of integers to read from the input.
 * @return vector<int> A vector containing the integers read from the input.
 */
vector<int> get_numbers_input(int length)
{
	vector<int> numbers{};
	int currentNumber;

	do
	{
		cin >> currentNumber;
		numbers.push_back(currentNumber);
		length--;
	} while (length > 0 && cin.peek() == ' ');

	return numbers;
}

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

struct node *lca(struct node *root, int v1, int v2)
{
	if (root == NULL)
	{
		return NULL;
	}
	cout << root->key << " " << v1 << " " << v2 << endl;
	if (root->key == v1 || root->key == v2)
	{
		return root;
	}
	if (
			(root->key > v1 && root->key <= v2) ||
			(root->key > v2 && root->key <= v1))
	{
		return root;
	}
	if (root->key > v1 && root->key > v2)
	{
		return lca(root->left, v1, v2);
	}
	if (root->key <= v1 && root->key <= v2)
	{
		return lca(root->right, v1, v2);
	}
	return NULL;
}

int main()
{
	int length;
	cin >> length;

	vector<int> numbers = get_numbers_input(length);

	int v1, v2;
	cin >> v1;
	cin >> v2;

	struct node *root = NULL;

	for (uint i = 0; i < numbers.size(); i++)
	{
		root = insertNode(root, numbers[i]);
	}

	cout << lca(root, v1, v2)->key << endl;

	return 0;
}