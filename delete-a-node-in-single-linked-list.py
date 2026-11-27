# Linked List Delete at Position
# Platform: GFG
# Difficulty: Easy
# Topics: Linked List

import re


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head


def delete_at_position(head, x):
    if head is None or x <= 0:
        return head
    if x == 1:
        return head.next
    curr = head
    for _ in range(x - 2):
        if curr is None:
            return head
        curr = curr.next
    if curr is not None and curr.next is not None:
        curr.next = curr.next.next
    return head


def linked_list_to_list(head):
    res = []
    curr = head
    while curr is not None:
        res.append(curr.data)
        curr = curr.next
    return res


def parse_cases(lines):
    if not lines:
        return []
    if len(lines) == 1:
        vals = lines[0]
        if len(vals) >= 3 and vals[0] == len(vals) - 2:
            return [(vals[1:-1], vals[-1])]
        if len(vals) >= 2:
            return [(vals[:-1], vals[-1])]
        return []
    if len(lines) == 2:
        if len(lines[0]) == 1 and len(lines[1]) > 1:
            return [(lines[1], lines[0][0])]
        return [(lines[0], lines[1][0])]
    if len(lines) == 3:
        if len(lines[0]) == 1 and len(lines[2]) == 1:
            return [(lines[1], lines[2][0])]
        return [(lines[0], lines[1][0])]

    cases = []
    if len(lines[0]) == 1:
        t = lines[0][0]
        idx = 1
        for _ in range(t):
            if (
                idx + 2 < len(lines)
                and len(lines[idx]) == 1
                and len(lines[idx + 1]) == lines[idx][0]
                and len(lines[idx + 2]) == 1
            ):
                cases.append((lines[idx + 1], lines[idx + 2][0]))
                idx += 3
            elif idx + 1 < len(lines):
                cases.append((lines[idx], lines[idx + 1][0]))
                idx += 2
    return cases


def main():
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        nums = [int(v) for v in re.findall(r'-?\d+', line)]
        if nums:
            lines.append(nums)

    for arr, x in parse_cases(lines):
        head = build_linked_list(arr)
        head = delete_at_position(head, x)
        res = linked_list_to_list(head)
        print(" -> ".join(map(str, res)))


if __name__ == "__main__":
    main()