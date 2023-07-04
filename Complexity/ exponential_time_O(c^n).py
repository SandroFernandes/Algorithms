import time
import matplotlib.pyplot as plt


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def show_and_plot():
    sizes = range(1, 31)
    times = []

    for size in sizes:
        start_time = time.time()
        fibonacci(size)
        end_time = time.time()
        times.append(end_time - start_time)

    plt.plot(sizes, times)
    plt.xlabel('Size of Input')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity of Recursive Fibonacci')
    plt.show()


if __name__ == '__main__':
    show_and_plot()
