class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Error: Stack is empty"

    def display(self):
        return self.stack

    def is_empty(self):
        return len(self.stack) == 0
