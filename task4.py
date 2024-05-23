class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Error"
    def display(self):
        return self.stack
    def is_empty(self):
        return len(self.stack) == 0
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.display())
popped_element = stack.pop()
print(popped_element)
print(stack.display())
