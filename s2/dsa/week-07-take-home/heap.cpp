#include <iostream>
#include <vector>
#include <stdlib.h>
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
   int queries;
   cin >> queries;

   int n = 0;
   int *arr = (int *)malloc(sizeof(int) * n);

   for (int i = 0; i < queries; i++)
   {
      int operation, value;
      cin >> operation;

      switch (operation)
      {
      case 1:
         // resize
         n++;
         arr = (int *)realloc(arr, sizeof(int) * n);

         // insert
         cin >> value;
         arr[n - 1] = value;

         // build max heap
         buildMaxHeap(arr, n);
         break;
      case 2:
         // find index
         cin >> value;
         int item_to_be_deleted_index;

         for (int j = 0; j < n; j++)
         {
            if (arr[j] == value)
            {
               item_to_be_deleted_index = j;
               break;
            }
         }

         // remove
         swap(arr[item_to_be_deleted_index], arr[n - 1]);
         heapify(arr, n, item_to_be_deleted_index);

         // resize
         n--;
         arr = (int *)realloc(arr, sizeof(int) * n);

         break;
      case 3:
         heapSort(arr, n);
         cout << arr[0];
         break;
      default:
         cout << "Unknown operation\n";
         break;
      }
   }
}