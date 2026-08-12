from math import floor
nums = [10, 8, 4, 21, 17, 6, 3]


def iLeftChild(i):
    return 2*i + 1


def iRightChild(i):
    return 2*i + 2


def iParent(i):
    return floor((i - 1) / 2)


def heapify(arr):
    start = iParent(len(arr)-1) + 1  # parent of the last element
    while start > 0:
        start -= 1
        siftDown(arr, start, len(arr))


def siftDown(arr, root, end):
    while iLeftChild(root) < end:
        child = iLeftChild(root)
        if child + 1 < arr[-1] and arr[child] < arr[child + 1]:
            child = child + 1

        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child


def heap_sort(arr):
    heapify(arr)
    end = len(arr)
    while end > 1:
        end = end - 1
        arr[end], arr[0] = arr[0], arr[end]
        siftDown(arr, 0, end)
        print(arr)


print(heap_sort(nums))
