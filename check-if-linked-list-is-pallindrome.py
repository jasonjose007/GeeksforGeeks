# Palindrome Linked List
# Platform: GFG
# Difficulty: Medium
# Topics: Linked List, palindrome

import sys
import re

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        # Find the middle of the linked list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        curr = slow.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Compare the first half and the reversed second half
        p1 = head
        p2 = prev
        is_pal = True
        while p2:
            if p1.data != p2.data:
                is_pal = False
                break
            p1 = p1.next
            p2 = p2.next

        return is_pal

def main():
    raw_input = sys.stdin.read().strip()
    if not raw_input:
        return

    lines = [line.strip() for line in raw_input.splitlines() if line.strip()]
    if not lines:
        return

    # Determine test cases
    test_cases = []
    try:
        first_val = int(lines[0])
        if first_val == len(lines) - 1 and first_val > 0:
            test_cases = lines[1:]
        elif first_val * 2 == len(lines) - 1 and first_val > 0:
            test_cases = lines[2::2]
        else:
            test_cases = lines
    except ValueError:
        test_cases = lines

    for line in test_cases:
        nums = [int(x) for x in re.findall(r'-?\d+', line)]
        if not nums:
            continue
        if nums == nums[::-1]:
            print("true")
        else:
            print("false")

if __name__ == '__main__':
    main()