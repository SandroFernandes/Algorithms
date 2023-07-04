import time
import matplotlib.pyplot as plt
import random
import heapq


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]


def show_and_plot():
    """Show the time complexity of merge sort """

    # can change the range of sizes to see how the time complexity changes
    # Higher the range, the longer it takes to run, but the more accurate the graph
    sizes = range(1000, 20000, 100)
    times = []

    for size in sizes:
        arr = [random.random() for _ in range(size)]
        start_time = time.time()
        merge_sort(arr)
        end_time = time.time()
        times.append(end_time - start_time)

    plt.plot(sizes, times)
    plt.xlabel('Size of Input')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity of Merge Sort')
    plt.show()


if __name__ == '__main__':
    show_and_plot()
