nums = [2, 8, 5, 3, 9, 4]


def insertion_sort(a_list):
    start_index = 1
    while start_index < len(a_list):
        pointer = start_index
        while pointer > 0 and a_list[pointer - 1] > a_list[pointer]:
            # swap the position
            a_list[pointer], a_list[pointer -
                                    1] = a_list[pointer-1], a_list[pointer]
            pointer -= 1
        print(f"{start_index}-sorted", a_list)
        start_index += 1


insertion_sort(nums)
