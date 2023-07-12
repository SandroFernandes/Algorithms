# binary search algorithm using recursion


def binary_search(arr, low, high, x, tries=1):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid, tries
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x, tries=tries + 1)
        else:
            return binary_search(arr, mid + 1, high, x, tries=tries + 1)
    else:
        return -1, tries


print('Search for {} found in {} tries.'.format(*binary_search(range(0, 1025), 0, 1025, 4)))
