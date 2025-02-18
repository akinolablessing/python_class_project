class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Cannot pop from an empty stack")
