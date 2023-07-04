import time
import matplotlib.pyplot as plt
import itertools
import random


def all_permutations(lst):
    return list(itertools.permutations(lst))


def show_and_plot():
    """Show the time complexity of all permutations """

    # Can change the range of sizes to see how the time complexity changes
    sizes = range(1, 12)
    times = []

    for size in sizes:
        lst = [random.random() for _ in range(size)]
        start_time = time.time()
        all_permutations(lst)
        end_time = time.time()
        times.append(end_time - start_time)

    plt.plot(sizes, times)
    plt.xlabel('Size of Input')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity of All Permutations')
    plt.show()


if __name__ == '__main__':
    show_and_plot()
