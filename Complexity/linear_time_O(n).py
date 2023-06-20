# Examples of linear time complexity O(n)

def find_item(lst, item):
    for i in lst:
        if i == item:
            return True
    return False


def compute_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total


def search_bst(node, target):
    if node is None or node.value == target:
        return node
    if target < node.value:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)


def insert_end(lst, item):
    lst.append(item)


def sort_list(lst):
    lst.sort()
