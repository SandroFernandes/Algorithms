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

# Options for the user to choose from
options = ["O(1)", "O(n)", "O(log n)", "O(n log n)", "O(n^2)"]

# Go through the code snippets and collect the user's answers
correct = 0
total = len(snippets)
for i, snippet in enumerate(snippets):
    print(f"\nFunction {i + 1}:")
    print(snippet)
    print("What is the time complexity of this function?")
    for j, option in enumerate(options):
        print(f"{j + 1}. {option}")
    while True:
        try:
            answer = int(input("Choose the correct answer (1-5): ")) - 1
            if 0 <= answer < len(options):
                user_answer = options[answer]
                if user_answer == answers[i]:
                    print("Correct!\n")
                    correct += 1
                else:
                    print(f"Oops! The correct answer is {answers[i]}\n")
                break
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Provide final score and feedback
print(f"You got {correct} out of {total} correct.")

score = correct / total
if score == 1:
    print("Excellent job! You have a strong understanding of time complexity.")
elif score >= 0.8:
    print("Great job! You have a good understanding of time complexity, just a bit more to master.")
elif score >= 0.6:
    print("Good job! You have a fair understanding of time complexity. Keep practicing to improve.")
else:
    print("Don't worry, understanding time complexity can be tricky. Keep studying and practicing, you'll get there!")
