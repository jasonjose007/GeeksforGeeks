# Max Heap implementation
# Platform: GFG
# Difficulty: Easy
# Topics: Heap, STL

import heapq


class maxHeap:

    def __init__(self):
        self.heap = []

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, -x)

    def pop(self) -> None:
        if self.heap:
            heapq.heappop(self.heap)

    def peek(self) -> int:
        if not self.heap:
            return -1
        return -self.heap[0]

    def size(self) -> int:
        return len(self.heap)