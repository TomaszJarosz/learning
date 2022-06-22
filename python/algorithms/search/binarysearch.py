def binary_search_sam(sorted_list, value_to_search):
    left_edge, right_edge = 0, len(sorted_list) - 1
    while left_edge <= right_edge:
        middle = (left_edge + right_edge) // 2
        if sorted_list[middle] == value_to_search:
            return middle
        if sorted_list[middle] < value_to_search:
            left_edge = middle + 1
        else:
            right_edge = middle - 1


def binary_search_sam_recursive(sorted_list, value_to_search, left_edge, right_edge):
    # left_edge, right_edge = 0, len(sorted_list) - 1
    middle = (left_edge + right_edge) // 2
    if sorted_list[middle] == value_to_search:
        return middle
    if sorted_list[middle] < value_to_search:
        left_edge = middle + 1
    else:
        right_edge = middle - 1
    return binary_search_sam_recursive(sorted_list, value_to_search, left_edge, right_edge)
