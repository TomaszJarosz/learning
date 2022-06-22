def first_last_index(sorted_array, target):
    first_position, last_position = -1, -1
    if len(sorted_array) < 2:
        return [-1, -1]

    # # O(n) linear
    # for index in range(len(sorted_array)):
    #     if sorted_array[index] == target:
    #         if first_position == -1:
    #             first_position = index
    #         last_position = index
    #         if last_position != -1 and sorted_array[index] != target:
    #             break

    # O(logn(n))
    left_edge = 0
    right_edge = len(sorted_array) - 1
    while left_edge <= right_edge:
        middle = (left_edge + right_edge) // 2
        if sorted_array[middle] == target and sorted_array[middle - 1] != target:
            first_position = middle
            break
        elif sorted_array[middle] < target:
            left_edge = middle + 1
        else:
            right_edge = middle - 1

    left_edge = 0
    right_edge = len(sorted_array) - 1
    while left_edge <= right_edge:
        middle = (left_edge + right_edge) // 2
        if sorted_array[middle] == target and sorted_array[middle + 1] != target:
            last_position = middle
            break
        elif sorted_array[middle] < target:
            left_edge = middle + 1
        else:
            right_edge = middle - 1

    return [first_position, last_position]
