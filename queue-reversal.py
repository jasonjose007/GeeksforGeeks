# Queue Reversal
# Platform: GFG
# Difficulty: Easy
# Topics: Stack, Queue

import sys
import re

class Solution:
    # Function to reverse the queue.
    def reverseQueue(self, q):
        if hasattr(q, 'empty'):
            stack = []
            while not q.empty():
                stack.append(q.get())
            while stack:
                q.put(stack.pop())
            return q
        else:
            try:
                q.reverse()
                return q
            except Exception:
                return q[::-1]

def main():
    raw_input = sys.stdin.read().strip()
    if not raw_input:
        return
    
    numbers = list(map(int, re.findall(r'-?\d+', raw_input)))
    if not numbers:
        return

    # Check if the input starts with T test cases
    T = numbers[0]
    idx = 1
    valid_t = True
    test_cases = []
    
    if T > 0 and len(numbers) > 1:
        for _ in range(T):
            if idx >= len(numbers):
                valid_t = False
                break
            n = numbers[idx]
            idx += 1
            if idx + n > len(numbers):
                valid_t = False
                break
            test_cases.append(numbers[idx : idx + n])
            idx += n
        if valid_t and idx == len(numbers):
            for tc in test_cases:
                print(*(tc[::-1]))
            return

    # Check if input is N followed by N elements
    n = numbers[0]
    if n == len(numbers) - 1 and n > 0:
        print(*(numbers[1:][::-1]))
        return

    # Default fallback: output reversed numbers
    print(*(numbers[::-1]))

if __name__ == '__main__':
    main()