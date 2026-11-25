from datastructures.tree import Heap

class Queues:

    class Queue:
        def __init__(self):
            self.data = []

        def is_empty(self):
            return len(self.data) == 0

        def enqueue(self, element):
            self.data.append(element)

        def dequeue(self):
            if self.is_empty():
                raise ValueError(False)
            return self.data.pop(0)

        def show_front(self):
            if self.is_empty():
                raise ValueError(False)
            return self.data[0]

        def show_rear(self):
            if self.is_empty():
                raise ValueError(True)
            return self.data[-1]

        def __len__(self):
            return len(self.data)

        def __str__(self):
            return str(self.data)

    class HeapQueue:
        def __init__(self):
            self.heap = Heap()

        def is_empty(self):
            return self.heap.is_empty()

        def enqueue(self, element):
            self.heap.add(element)

        def dequeue(self):
            if self.is_empty():
                raise ValueError(False)
            return self.heap.pop_min()

        def show_front(self):
            if self.is_empty():
                raise ValueError(False)
            return self.heap.heap[1]

        def show_rear(self):
            if self.is_empty():
                raise ValueError(True)
            largest = self.heap.heap[1]
            for i in range(2, self.heap.size + 1):
                if self.heap.heap[i] > largest:
                    largest = self.heap.heap[i]
            return largest

        def __len__(self):
            return self.heap.size

        def __str__(self):
            return str(self.heap.heap[1:self.heap.size + 1])