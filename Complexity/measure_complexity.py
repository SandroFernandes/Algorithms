import numpy as np
import matplotlib.pyplot as plt
from timeit import timeit
from constant_time import access_element
from linear_time_O_n import compute_sum

# Create lists of different sizes
print('Allocating memory...')
small = list(range(10_000))
medium = list(range(100_000))
large = list(range(10_000_000))
extra_large = list(range(100_000_000))
print('Memory allocated.')


def plot_measurements(x, y, polynomial):
    plt.scatter(x, y, color='blue')
    plt.plot(x, polynomial(x), color='red')
    plt.show()


def measure_time_constant():
    measurements = []
    # depending on your machine, you may need to adjust the rounding
    # Measures may vary depending on what your machine is doing,
    # try running this script a few times to get the constant time measurements
    round_to = 3

    print('Starting measurements...')

    measurements.append(round(timeit(stmt='access_element(small, 10)', globals=globals(), number=100_000), round_to))
    measurements.append(round(timeit(stmt='access_element(medium, 10)', globals=globals(), number=100_000), round_to))
    measurements.append(round(timeit(stmt='access_element(large, 10)', globals=globals(), number=100_000), round_to))
    measurements.append(round(timeit(stmt='access_element(extra_large, 10)', globals=globals(), number=100_000), round_to))

    print('Measurements complete.')

    x = np.array(range(len(measurements)))
    y = np.array(list(measurements))

    coefficients = np.polyfit(x, y, 1)
    polynomial = np.poly1d(coefficients)

    plot_measurements(x, y, polynomial)


if __name__ == '__main__':
    measure_time_constant()
