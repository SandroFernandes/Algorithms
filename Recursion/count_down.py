import time


def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        time.sleep(1)  # Adds a 1-second delay
        countdown(n - 1)


countdown(5)
