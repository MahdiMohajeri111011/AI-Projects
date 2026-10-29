class Heap:

    def __init__(self, max_size):
        self.max_size = max_size
        self.heap = [None] * (max_size + 1)
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def parent(self, i):
        return i // 2

    def left_child(self, i):
        return 2 * i

    def right_child(self, i):
        return 2 * i + 1

    def add(self, value):
        if not self.is_full():
            self.size += 1
            i = self.size
            self.heap[i] = value
            self.heapfy_up(i)
            return True
        return False

    def heapfy_up(self, i):
        while i > 1 and self.heap[self.parent(i)] > self.heap[i]:   # ← برعکس شد
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def pop_min(self):                                              # ← اسم عوض شد
        if not self.is_empty():
            min_element = self.heap[1]
            self.heap[1] = self.heap[self.size]
            self.size -= 1
            self.heapfy_down(1)
            return min_element
        return False

    def heapfy_down(self, i):
        while True:

            left = self.left_child(i)
            right = self.right_child(i)
            smallest = i                 # ← largest → smallest

            if left <= self.size and self.heap[left] < self.heap[smallest]:    # ← >
                smallest = left

            if right <= self.size and self.heap[right] < self.heap[smallest]:  # ← >
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest