# List of code snippets to present to the user
snippets = [
    """
def find_item(lst, item):
    for i in lst:
        if i == item:
            return True
    return False
    """,

    """
def compute_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total
    """,

    """
def search_bst(node, target):
    if node is None or node.value == target:
        return node
    if target < node.value:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)
    """,

    """
def insert_end(lst, item):
    lst.append(item)
    """,

    """
def sort_list(lst):
    lst.sort()
    """
]

# List of correct answers for the time complexity of the functions
answers = ["O(n)", "O(n)", "O(log n)", "O(1)", "O(n log n)"]

# Go through the code snippets and collect the user's answers
user_answers = []
for i, snippet in enumerate(snippets):
    print(f"Function {i + 1}:")
    print(snippet)
    answer = input("What is the time complexity of this function? ")
    user_answers.append(answer)

# Check the user's answers against the correct answers
correct = 0
for i, (user_answer, correct_answer) in enumerate(zip(user_answers, answers)):
    if user_answer == correct_answer:
        correct += 1
    else:
        print(f"Function {i + 1} has a time complexity of {correct_answer}, not {user_answer}.")

print(f"You got {correct} out of {len(snippets)} correct.")
