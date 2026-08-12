#include <iostream>
using namespace std;

/**
 * Parent index of a child node
 * @param child_index index of the child node
 * @returns  index of the parent node
 */
int parentIndex(int child_index)
{
   return child_index >> 1; // floor division of 2
}

/**
 * Index of the left chlid for the given node
 * @param parent_index index of the node
 * @return index of the left child
 */
int leftChildIndex(int parent_index)
{
   return (parent_index << 1) + 1;
}

/**
 * Index of the right chlid for the given node
 * @param parent_index index of the node
 * @return index of the right child
 */
int rightChildIndex(int parent_index)
{
   return (parent_index + 1) << 1;
}

/**
 * Restores heap property for a subtree in-place
 * @param arr[] tree to be heapified
 * @param n total number of items in arr
 * @param root index of root of the subtree
 */
void heapify(int arr[], int n, int root)
{
   // find the largest child
   int index__left_child = leftChildIndex(root);
   int largest_index;
   if (index__left_child < n && arr[index__left_child] > arr[root])
   {
      largest_index = index__left_child;
   }
   else
   {
      largest_index = root;
   }
   int index__right_child = rightChildIndex(root);
   if (index__right_child < n && arr[index__right_child] > arr[largest_index])
   {
      largest_index = index__right_child;
   }

   if (largest_index == root)
   {
      return;
   }

   // if the largest is not the root,
   swap(arr[root], arr[largest_index]);
   heapify(arr, n, largest_index);
}

/**
 * Recursively build a max heap in-place
 * @param arr[] array to be heapified
 * @param n total number of items in arr
 */
void buildMaxHeap(int arr[], int n)
{
   for (int i = (n >> 1) - 1; i >= 0; i--)
   {
      heapify(arr, n, i);
   }
}

/**
 * Sorts an array in-place using a max heap
 */
void heapSort(int arr[], int n)
{
   buildMaxHeap(arr, n);

   for (int i = n - 1; i >= 1; i--)
   {
      swap(arr[0], arr[i]);
      heapify(arr, i, 0);
   }
}

/* print contents of array */
void displayArray(int arr[], int n)
{
   for (int i = 0; i < n; ++i)
      cout << arr[i] << " ";
   cout << "\n";
}

// main program
int main()
{
   int heap_arr[] = {4, 17, 3, 12, 9, 6};
   int n = sizeof(heap_arr) / sizeof(heap_arr[0]);
   cout << "Input array" << endl;
   displayArray(heap_arr, n);

   heapSort(heap_arr, n);

   cout << "Sorted array" << endl;
   displayArray(heap_arr, n);
}