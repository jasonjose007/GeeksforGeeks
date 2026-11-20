# Stack using Queue
# Platform: GFG
# Difficulty: Medium
# Topics: Stack, Queue, Design-Pattern

from collections import deque

class Stack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        if self.q:
            return self.q.popleft()

    def top(self) -> int:
        if self.q:
            return self.q[0]
        return -1

    def size(self) -> int:
        return len(self.q)