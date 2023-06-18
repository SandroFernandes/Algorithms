# generate all binary strings of length n

def generate_binary_strings(n, arr, i):
    if i == n:
        print(arr)
        return
    else:
        arr[i] = 0
        generate_binary_strings(n, arr, i + 1)
        arr[i] = 1
        generate_binary_strings(n, arr, i + 1)


print(generate_binary_strings(3, [0, 0, 0], 0))