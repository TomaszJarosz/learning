def quicksort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    else:
        pivot = unsorted_list.pop()
        lower, greater = [], []
        for i in unsorted_list:
            if i < pivot:
                lower.append(i)
            else:
                greater.append(i)
    return quicksort(lower) + [pivot] + quicksort(greater)
