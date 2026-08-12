def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        print(f"checking {mid} (searching in {first}-{last})")
        if a_list[mid] == item:
            found = True
        else:
            if item < a_list[mid]:
                last = mid - 1  # search in first half
            else:
                first = mid + 1  # search in second half

    if found:
        return mid
    else:
        return None


print(binary_search(
    [0.2, 1, 2, 3, 4, 5,  8, 9, 10, 655],
    8
))
