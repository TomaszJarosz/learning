def selection_sort(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list
    for i in range(len(unsorted_list)):
        smallest_index = i
        for j in range(i + 1, len(unsorted_list)):
            if (unsorted_list[j]) < unsorted_list[smallest_index]:
                smallest_index = j
        unsorted_list[smallest_index], unsorted_list[i] = unsorted_list[i], unsorted_list[smallest_index]
    return unsorted_list
