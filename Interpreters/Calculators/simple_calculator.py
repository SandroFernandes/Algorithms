# This was way back to do it.
# To simplify the code, we use the tokenize module to split the input into tokens.
# The tokenizer itself will be more code than the calculator.
# An infix to post fix calculator that uses a stack to evaluate expressions
# can handle numbers and operators +, -, *, /, ^, (, )
# no unary operators
# no functions
# no constants
# The tokenizer can handle variables, but not the calculator

import tokenize
from io import StringIO
from Utils.stack import Stack


class Calculator:
    # Set the priority level of the operators

    operators = {"^", "/", "*", "+", "-"}
    precedence = {"^": 4,
                  "/": 3,
                  "*": 3,
                  "+": 2,
                  "-": 2,
                  "(": 1}

    def __init__(self, exp_str):
        self.exp_str = exp_str
        self.infix_tokens = []
        self.postfix_tokens = []
        self.prefix_tokens = []
        self.value = 0

        self.tokenize()
        self.infix_to_postfix()
        self.evaluate_postfix()

    def __str__(self):
        return self.exp_str

    def __repr__(self):
        return f'{self.exp_str}   {self.postfix_tokens}  {self.prefix_tokens}'

    def tokenize(self):
        for x in tokenize.generate_tokens(StringIO(self.exp_str).readline):
            if x.string:
                self.infix_tokens.append(x.string)

    def infix_to_postfix(self):

        stack = Stack()
        stack.push("(")

        self.infix_tokens.append(")")

        while self.infix_tokens:

            token = self.infix_tokens.pop(0)

            if token == "(":
                stack.push(token)

            elif token == ")":

                while stack.peek() != "(":
                    self.postfix_tokens.append(stack.pop())
                stack.pop()

            elif token in self.operators:

                while stack and self.precedence[stack.peek()] >= self.precedence[token]:
                    self.postfix_tokens.append(stack.pop())
                stack.push(token)

            else:

                self.postfix_tokens.append(token)

        if not stack.is_empty():
            raise ValueError("Invalid expression")

    def convert_to_number(self, token):
        try:
            return int(token)
        except ValueError:
            return float(token)
        except ValueError:
            raise ValueError(f"Invalid number {token}")

    def evaluate_postfix(self):
        stack = Stack()
        for token in self.postfix_tokens:
            if token in self.operators:

                op1 = self.convert_to_number(stack.pop())
                op2 = self.convert_to_number(stack.pop())

                match token:
                    case "^":
                        stack.push(op2 ** op1)
                    case "/":
                        stack.push(op2 / op1)
                    case "*":
                        stack.push(op2 * op1)
                    case "+":
                        stack.push(op2 + op1)
                    case "-":
                        stack.push(op2 - op1)
                    case _:
                        raise ValueError(f"Invalid operator {token}")
            else:
                stack.push(token)

        self.value = stack.pop()

        if not stack.is_empty():
            raise ValueError("Invalid expression")

    def postfix_expression(self):
        return self.postfix_tokens


if __name__ == "__main__":
    expressions = [
        "2+2",
        "2+3*4",
        "2^3^2",
        "2*3/4",
        "10 * 2 + 6",
        "20*7-0 +(4-2*5)-10+40",
        "(12) + 3 * 4",
        "3.14 + 2.71",
        "2.71 * 10 + 3.14 * 20",
        # the tokenizer can handle variables but the calculator can't
        # "A * B- (C + D) + E",
        # "(A + B) * (C -D)",

    ]
    for expression in expressions:
        exp = Calculator(expression)
        print(f'Expression:{" ".join(exp.postfix_expression())}')
        print(f'Postfix expression:{" ".join(exp.postfix_expression())}')
        print(f'Result:{exp.value}')
        print()

    while True:
        exp = input("Enter an expression: ")
        if exp == "quit":
            break
        try:
            calc = Calculator(exp)
            print(f'Expression:{" ".join(calc.postfix_expression())}')
            print(f'Postfix expression:{" ".join(calc.postfix_expression())}')
            print(f'Result:{calc.value}')
        except ValueError as e:
            print(e)
        print()
