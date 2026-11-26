# Insert at Middle of Linked List
# Platform: GFG
# Difficulty: Easy
# Topics: Linked List

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def insertInMid(self, head, node):
        if not isinstance(node, Node):
            node = Node(node)
        if head is None:
            return node
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        node.next = slow.next
        slow.next = node
        return head

def insertInMid(head, node):
    return Solution().insertInMid(head, node)

if __name__ == '__main__':
    input_text = sys.stdin.read().strip()
    if input_text:
        import re
        tokens = input_text.split()
        # Check if first token might be number of test cases
        # Standard GfG: T test cases, each with N, then N elements, then x
        pos = 0
        
        def build_and_run(vals, x):
            head = None
            tail = None
            for v in vals:
                new_node = Node(v)
                if not head:
                    head = tail = new_node
                else:
                    tail.next = new_node
                    tail = new_node
            head = Solution().insertInMid(head, Node(x))
            res = []
            curr = head
            while curr:
                res.append(str(curr.data))
                curr = curr.next
            print(" ".join(res))

        # Check if format is '->' style from example
        if '->' in input_text or '=' in input_text:
            lines = [line.strip() for line in input_text.splitlines() if line.strip()]
            i = 0
            while i < len(lines):
                line = lines[i]
                nums = re.findall(r'-?\d+', line)
                if len(nums) > 1 and i + 1 < len(lines):
                    x_nums = re.findall(r'-?\d+', lines[i + 1])
                    if x_nums:
                        vals = [int(n) for n in nums]
                        x = int(x_nums[-1])
                        build_and_run(vals, x)
                        i += 2
                        continue
                elif len(nums) >= 2:
                    vals = [int(n) for n in nums[:-1]]
                    x = int(nums[-1])
                    build_and_run(vals, x)
                i += 1
        else:
            # Token-based parsing
            int_tokens = [int(tok) for tok in tokens if re.fullmatch(r'-?\d+', tok)]
            idx = 0
            if len(int_tokens) >= 1:
                # Try parsing as T test cases
                T = int_tokens[0]
                temp_idx = 1
                can_be_t = True
                cases = []
                for _ in range(T):
                    if temp_idx < len(int_tokens):
                        n = int_tokens[temp_idx]
                        if temp_idx + 1 + n < len(int_tokens):
                            vals = int_tokens[temp_idx + 1 : temp_idx + 1 + n]
                            x = int_tokens[temp_idx + 1 + n]
                            cases.append((vals, x))
                            temp_idx += 2 + n
                        else:
                            can_be_t = False
                            break
                    else:
                        can_be_t = False
                        break
                
                if can_be_t and temp_idx == len(int_tokens) and cases:
                    for vals, x in cases:
                        build_and_run(vals, x)
                else:
                    # Single testcase: N elements then x, or N then elements then x
                    if len(int_tokens) >= 3 and int_tokens[0] == len(int_tokens) - 2:
                        n = int_tokens[0]
                        vals = int_tokens[1 : 1 + n]
                        x = int_tokens[1 + n]
                        build_and_run(vals, x)
                    else:
                        vals = int_tokens[:-1]
                        x = int_tokens[-1]
                        build_and_run(vals, x)