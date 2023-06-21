import heapq


# O(log n) is the best time complexity for search algorithms

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# insert code here to test the binary_search recursive function
# and compare its output to the iterative function


def exponentiation(base, power):
    if power == 0:
        return 1

    result = 1
    while power > 0:
        if power % 2 == 1:
            result *= base
        base *= base
        power //= 2

    return result


# again, insert code here to test the exponentiation recursive function
# and compare its output to the iterative function

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal(root):
    """ Expected output:1 2 3 4 5 6 7"""
    if root is None:
        return

    inorder_traversal(root.left)
    print(root.value, end=' ')
    inorder_traversal(root.right)


if __name__ == '__main__':
    # Create a binary search tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    # Perform in-order traversal
    print("In-order traversal:")
    inorder_traversal(root)

    # Create an empty heap
    heap = []

    # Insert elements into the heap
    heapq.heappush(heap, 4)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 7)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 2)

    print("Heap:", heap)

    # Extract the minimum element from the heap
    min_element = heapq.heappop(heap)
    print("Minimum Element:", min_element)

    # Peek at the minimum element without removing it
    min_element = heap[0]
    print("Peek at Minimum Element:", min_element)
    """
        Heap: [1, 2, 7, 4, 3]
        Minimum Element: 1
        Peek at Minimum Element: 2
    """
