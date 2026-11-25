class Heap:

    def __init__(self, max_size=None):
        self.max_size = max_size
        self.heap = [None]
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return False

    def parent(self, i):
        return i // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def add(self, value):
        self.heap.append(value)
        self.size += 1
        self.heapfy_up(self.size)
        return True

    def heapfy_up(self, i):
        while i > 1 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def pop_min(self):
        if not self.is_empty():
            min_element = self.heap[1]
            last_element = self.heap.pop()
            self.size -= 1
            if not self.is_empty():
                self.heap[1] = last_element
                self.heapfy_down(1)
            return min_element
        return False

    def heapfy_down(self, i):
        while True:

            left = self.left_child(i)
            right = self.right_child(i)
            smallest = i

            if left <= self.size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right <= self.size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest