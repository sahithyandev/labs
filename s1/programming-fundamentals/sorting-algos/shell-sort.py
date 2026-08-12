nums = [10, 8, 4, 21, 17, 6, 3]


def gap_insertion_sort(a_list, start_index, gap):
    while start_index < len(a_list):
        pointer = start_index
        while pointer >= gap and a_list[pointer - gap] > a_list[pointer]:
            # swap the position
            a_list[pointer], a_list[pointer - gap] = \
                a_list[pointer-gap], a_list[pointer]

            pointer -= gap
        start_index += gap


def shell_sort(a_list):
    for gap in range(4, 0, -1):
        for starting_index in range(0, gap):
            gap_insertion_sort(a_list, starting_index, gap)

        print(f"{gap}-sorted", a_list)


shell_sort(nums)
