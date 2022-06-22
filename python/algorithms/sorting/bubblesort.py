def bubble_sort(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, len(unsorted_list) - 1):
            if unsorted_list[i] > unsorted_list[i + 1]:
                sorted = False
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
    return unsorted_list
