class Stack:
    def __init__(self):
        self.memory = []

    def push(self, item):
        self.memory.append(item)

    def pop(self):
        return self.memory.pop()

    def is_empty(self):
        return len(self.memory) == 0

    def peek(self):
        return self.memory[-1]

example = Stack()
example.push(1)
example.push(4)
example.push(9)

print("Peeked", example.peek())
