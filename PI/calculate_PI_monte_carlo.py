# https://en.wikipedia.org/wiki/Monte_Carlo_method
import random


def estimate_pi(num_samples):
    num_points_inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            num_points_inside_circle += 1

    pi_estimate = 4 * num_points_inside_circle / num_samples
    return pi_estimate


if __name__ == '__main__':
    print(estimate_pi(100_000_000))
