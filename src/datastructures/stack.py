class Stack:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        return 0, None

    def top_element(self):
        if not self.is_empty():
            return self.data[-1]
        return 0, None

    def show(self):
        for element in self.data:
            print(element)