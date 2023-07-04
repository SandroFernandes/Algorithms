import time
import matplotlib.pyplot as plt
import random


# Common example of an algorithm with polynomial time complexity O(n^c) is the Bubble Sort algorithm.
# Bubble Sort has a worst-case and average time complexity of O(n^c), where n is the number of items being sorted.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def show_and_plot():
    """Show the time complexity of bubble sort """

    # Can change the range of sizes to see how the time complexity changes
    # Higher the range, the longer it takes to run, but the more accurate the graph
    sizes = range(500, 5000, 100)
    times = []

    for size in sizes:
        arr = [random.random() for _ in range(size)]
        start_time = time.time()
        bubble_sort(arr)
        end_time = time.time()
        times.append(end_time - start_time)

    plt.plot(sizes, times)
    plt.xlabel('Size of Input')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity of Bubble Sort')
    plt.show()


if __name__ == '__main__':
    show_and_plot()
