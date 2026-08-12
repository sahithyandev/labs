nums = [2, 8, 5, 3, 9, 4]


def recursive_sequential_search(a_list, item, offset=0):
    if len(a_list) == offset - 1:
        return False

    if a_list[offset] == item:
        return True

    return recursive_sequential_search(a_list, item, offset+1)


print(recursive_sequential_search(nums, 9))
