nums = [100, 2, -5, 10, 1.2, 100, 9, 11]


def bubble_sort(arr: list[int | float]):
    sorted_index_count = 0
    while sorted_index_count < len(arr):
        for i in range(len(arr)-sorted_index_count-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        sorted_index_count += 1


bubble_sort(nums)
print(nums)
