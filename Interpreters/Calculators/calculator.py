# An infix to post fix calculator that uses a stack to evaluate expressions


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
        self.postfix_to_prefix()
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
                # Pop out all the operators from the stack and append them to
                # postfix expression till an opening bracket "(" is found

                while stack.peek() != "(":
                    self.postfix_tokens.append(stack.pop())
                stack.pop()

            elif token in self.operators:
                # Pop out the operators with higher precedence from the top of the
                # stack and append them to the postfix expression before
                # pushing the current operator onto the stack.
                while stack and self.precedence[stack.peek()] >= self.precedence[token]:
                    self.postfix_tokens.append(stack.pop())
                stack.push(token)

            else:
                # Positions of the operands do not change in the postfix
                # expression so append an operand as it is to the postfix expression
                self.postfix_tokens.append(token)

    def postfix_to_prefix(self):
        """ Convert postfix expression to prefix expression """
        reversed_postfix = self.postfix_tokens[::-1]

        stack = Stack()
        for token in reversed_postfix:
            if token in self.operators:
                stack.push(token)
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.push(token)
                stack.push(op1)
                stack.push(op2)

        self.prefix_tokens = stack.dump()

        if not stack.is_empty():
            raise ValueError("Invalid expression")

    def evaluate_postfix(self):
        stack = Stack()
        for token in self.postfix_tokens:
            if token in self.operators:

                op1 = float(stack.pop())
                op2 = float(stack.pop())

                # noinspection PyCompatibility
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

    def prefix_expression(self):
        return self.prefix_tokens


if __name__ == "__main__":
    expressions = [
        "2+2",
        "2+3*4",
        "2^3^2",
        "2*3/4",
        "10 * 2 + 6",
        "20*7-0 +(4-2*5)-10+40",
        "(12) + 3 * 4",
        # "A * B- (C + D) + E",
        # "(A + B) * (C -D)",
    ]
    for expression in expressions:
        exp = Calculator(expression)
        print(exp)
        print(exp.postfix_expression())
        print(exp.value)
        print()
