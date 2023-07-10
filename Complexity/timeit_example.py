import timeit

# Define the function and parameters
setup = """
def multiply(a, b):
    return a * b

a = 10
b = 20
"""

# Define the function call
stmt = "multiply(a, b)"

# Time the function
time = timeit.timeit(setup=setup, stmt=stmt, number=10000000)

print(f"Time taken: {time} seconds")
