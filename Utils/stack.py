# create a stack class

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def dump(self):
        tmp = self.stack
        self.stack = []
        return tmp

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

    def __repr__(self):
        return str(self.stack)