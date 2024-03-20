import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)


class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, -item)

    def pop(self):
        return -heapq.heappop(self.heap)

    def peek(self):
        return -self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)


min_heap = MinHeap()
min_heap.push(5)
min_heap.push(6)
min_heap.push(3)
min_heap.push(1)
min_heap.push(2)

print("Min heap elements:")
while min_heap.size() > 0:
    print(min_heap.pop())


max_heap = MaxHeap()
max_heap.push(5)
max_heap.push(8)
max_heap.push(3)
max_heap.push(1)
max_heap.push(2)

print("Max heap elements:")
while max_heap.size() > 0:
    print(max_heap.pop())
