nums = [98, 10, 8, 4, 21, 100, 1.2, 17, 6, 3]


def merge_sort(a_list):
    if len(a_list) <= 1:  # then it's sorted
        return a_list

    # break at the middle and sort
    mid_index = len(a_list)//2
    left_half = merge_sort(a_list[:mid_index])
    right_half = merge_sort(a_list[mid_index:])

    # merge the sides
    cursor_left = 0
    cursor_right = 0
    sorted_list = []

    # add the smallest of those
    while cursor_left < len(left_half) and cursor_right < len(right_half):
        if left_half[cursor_left] > right_half[cursor_right]:
            sorted_list.append(right_half[cursor_right])
            cursor_right += 1
        else:
            sorted_list.append(left_half[cursor_left])
            cursor_left += 1

    # add left over elements
    while cursor_left < len(left_half):
        sorted_list.append(left_half[cursor_left])
        cursor_left += 1
    while cursor_right < len(right_half):
        sorted_list.append(right_half[cursor_right])
        cursor_right += 1

    return sorted_list


print(merge_sort(nums))
