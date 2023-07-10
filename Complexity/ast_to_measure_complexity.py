# One common measure of code complexity that can be calculated using the AST
# is the cyclomatic complexity.
# Cyclomatic complexity is a software metric used to indicate the complexity of a program.
# It is a quantitative measure of the number of linearly
# independent paths through a program's source code.

import ast
from .constant_time import add


def cyclomatic_complexity(tree):
    complexity = 0
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.For, ast.While, ast.And, ast.Or)):
            complexity += 1
    return complexity + 1


def calculate_complexity(code):
    tree = ast.parse(code)
    return cyclomatic_complexity(tree)


code = """
def example(x):
    if x > 0:
        return x
    else:
        return -x
"""

print(calculate_complexity(code))  # Output: 2
