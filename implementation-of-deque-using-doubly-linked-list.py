# Implement Deque using DLL
# Platform: GFG
# Difficulty: Medium
# Topics: Circular Linked List, Deque

import ast


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def insertFront(self, x):
        new_node = Node(x)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def insertRear(self, x):
        new_node = Node(x)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def deleteFront(self):
        if self.front is None:
            return
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None

    def delete
Rear(self):
        if self.rear is None:
            return
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None

    def getFront
(self):
        if self.front is None:
            return -1
        return self.front.data

    def getRear(self):
        if self.rear is None:
            return -1
        return self.rear.data


def solve():
    lines = []
    while True:
        try:
            line = input().strip()
            if line:
                lines.append(line)
        except EOFError:
            break

    if not lines:
        return

    full_text = "\n".join(lines)
    is_list_input = "[" in full_text

    if is_list_input:
        expr = full_text.split("=", 1)[-1] if "=" in full_text else full_text
        start = expr.find("[")
        end = expr.rfind("]")
        queries = ast.literal_eval(expr[start:end + 1])
    else:
        first_tokens = lines[0].split()
        if len(first_tokens) == 1 and int(first_tokens[0]) == len(lines) - 1:
            queries = [list(map(int, line.split())) for line in lines[1:]]
        else:
            queries = [list(map(int, line.split())) for line in lines]

    dq = Deque()
    ans = []
    for q in queries:
        op = q[0]
        if op == 1:
            dq.insertFront(q[1])
        elif op == 2:
            dq.insertRear(q[1])
        elif op == 3:
            dq.deleteFront()
        elif op == 4:
            dq.deleteRear()
        elif op == 5:
            ans.append(dq.getFront())
        elif op == 6:
            ans.append(dq.getRear())

    if is_list_input:
        print(ans)
    else:
        print(" ".join(map(str, ans)))


if __name__ == "__main__":
    solve()