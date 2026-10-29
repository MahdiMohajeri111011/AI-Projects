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
            return self.data

    class HeapQueue:
        def __init__(self, max_size):
            self.heap = Heap(max_size)

        def is_empty(self):
            return self.heap.is_empty()

        def is_full(self):
            return self.heap.is_full()

        def enqueue(self, element):
            if self.heap.is_full():
                raise OverflowError("heap queue is full")
            return self.heap.add(element)

        def dequeue(self):
            if self.is_empty():
                raise IndexError("dequeue from empty heap queue")
            return self.heap.pop_min()

        def show_front(self):
            if self.is_empty():
                raise IndexError("front from empty heap queue")
            return self.heap.heap[1]

        def show_rear(self):
            if self.is_empty():
                raise IndexError("rear from empty heap queue")
            largest = self.heap.heap[1]
            for i in range(2, self.heap.size + 1):
                if self.heap.heap[i] > largest:
                    largest = self.heap.heap[i]
            return largest

        def __len__(self):
            return self.heap.size

        def __repr__(self):
            return f"HeapQueue({self.heap.heap[1:self.heap.size + 1]})"