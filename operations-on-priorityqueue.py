# Min Priority Queue Operations
# Platform: GFG
# Difficulty: Easy
# Topics: Java, Java-Collections, Heap

import heapq
import sys


class minPriorityQueue:

    def __init__(self):
        self.pq = []

    def push(self, x: int) -> None:
        heapq.heappush(self.pq, x)

    def pop(self) -> int:
        if not self.pq:
            return -1
        return heapq.heappop(self.pq)

    def peek(self) -> int:
        if not self.pq:
            return -1
        return self.pq[0]

    def isEmpty(self) -> bool:
        return len(self.pq) == 0

    def size(self) -> int:
        return len(self.pq)


if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    if input_data:
        import ast

        try:
            queries = ast.literal_eval(input_data)
        except Exception:
            # Fallback for alternative input formatting
            lines = [line.strip() for line in input_data.splitlines() if line.strip()]
            queries = []
            for line in lines:
                if line.startswith("[") and line.endswith("]"):
                    try:
                        queries = ast.literal_eval(line)
                        break
                    except Exception:
                        pass
                else:
                    parts = list(map(int, line.split()))
                    if parts:
                        queries.append(parts)

        q_obj = minPriorityQueue()
        res = []
        for q in queries:
            op = q[0]
            if op == 1:
                q_obj.push(q[1])
            elif op == 2:
                res.append(q_obj.pop())
            elif op == 3:
                res.append(q_obj.peek())
            elif op == 4:
                res.append(q_obj.isEmpty())
            elif op == 5:
                res.append(q_obj.size())

        out = []
        for val in res:
            if isinstance(val, bool):
                out.append("true" if val else "false")
            else:
                out.append(str(val))
        print("[" + ", ".join(out) + "]")