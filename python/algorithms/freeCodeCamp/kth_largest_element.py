import heapq


def kth_largest_element(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError('k should be in range: 1<= k <= len(given_array)')
    arr.sort()
    return arr[len(arr) - k]


def kth_largest_element_hepq(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError('k should be in range: 1<= k <= len(given_array)')

    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k - 1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)
