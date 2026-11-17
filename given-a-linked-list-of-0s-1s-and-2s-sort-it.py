# Sort Llinked List of 0s, 1s and 2s
# Platform: GFG
# Difficulty: Medium
# Topics: Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_list(values):
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head


def segregate(head):
    if not head or not head.next:
        return head

    zero_dummy = Node(0)
    one_dummy = Node(0)
    two_dummy = Node(0)

    zero = zero_dummy
    one = one_dummy
    two = two_dummy

    curr = head
    while curr:
        if curr.data == 0:
            zero.next = curr
            zero = zero.next
        elif curr.data == 1:
            one.next = curr
            one = one.next
        else:
            two.next = curr
            two = two.next
        curr = curr.next

    zero.next = one_dummy.next if one_dummy.next else two_dummy.next
    one.next = two_dummy.next
    two.next = None

    return zero_dummy.next


def print_list(head):
    res = []
    curr = head
    while curr:
        res.append(str(curr.data))
        curr = curr.next
    print(" ".join(res))


def main():
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

    if len(lines) == 1:
        test_cases = [lines[0]]
    elif len(lines) == 2:
        t0 = lines[0].replace("->", " ").split()
        if len(t0) == 1:
            test_cases = [lines[1]]
        else:
            test_cases = lines
    else:
        t0 = lines[0].replace("->", " ").split()
        if len(t0) == 1 and t0[0].isdigit():
            t = int(t0[0])
            if len(lines) == 1 + t:
                test_cases = lines[1:]
            elif len(lines) == 1 + 2 * t:
                test_cases = [lines[2 + 2 * i] for i in range(t)]
            else:
                test_cases = lines
        else:
            test_cases = lines

    for case in test_cases:
        values = list(map(int, case.replace("->", " ").split()))
        head = build_list(values)
        sorted_head = segregate(head)
        print_list(sorted_head)


if __name__ == "__main__":
    main()