nums = [100, 2, -5, 10, 1.2, 9, 11]


def selection_sort(arr: list[int | float]):
    for current_starting_index in range(len(arr)):
        smallest_index = current_starting_index
        for i in range(current_starting_index + 1, len(arr)):
            if arr[i] < arr[smallest_index]:
                smallest_index = i
        arr[smallest_index], arr[current_starting_index] = arr[current_starting_index], arr[smallest_index]


selection_sort(nums)
print(nums)
