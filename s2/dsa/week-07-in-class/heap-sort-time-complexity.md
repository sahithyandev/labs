The heap sort is implemented using a max heap. The heap structure is stored in the memory in an array. The array structure keeps the access time O(1). Parent and child indices can be calculated in O(1) time as well. The swaps between the elements also run in constant time.

First `heapify` function is used to restore the heap property of a tree. This function runs in O(log_2 n) time. This function is used in the `buildMaxHeap` function.

`buildMaxHeap` function builds a heap from the given array by recursively calling heapify from the last element. As it is iterating over each element and calling `heapify`, it takes O(n log_2 n).

In `heapSort`, a max heap is built using `buildMaxHeap`. After that, each element at the end is replaced with the first one, and heapify is called repeatedly. So the whole algorithm runs in O(n log_2 n).

The same logic applies when a min heap is used.