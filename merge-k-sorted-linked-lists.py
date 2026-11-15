# Merge K Sorted Linked Lists
# Platform: GFG
# Difficulty: Medium
# Topics: Linked List, Heap, Merge Sort, two-pointer-algorithm

import sys
import heapq

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def mergeKLists(self, arr):
        heap = []
        count = 0
        for head in arr:
            if head:
                heapq.heappush(heap, (head.data, count, head))
                count += 1
        
        dummy = Node(0)
        tail = dummy
        
        while heap:
            val, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.data, count, node.next))
                count += 1
                
        return dummy.next

def print_list(head):
    res = []
    curr = head
    while curr:
        res.append(str(curr.data))
        curr = curr.next
    print(" ".join(res))

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        it = iter(input_data)
        try:
            t = int(next(it))
        except StopIteration:
            t = 0
        for _ in range(t):
            k = int(next(it))
            arr = []
            for _ in range(k):
                n = int(next(it))
                dummy = Node(0)
                tail = dummy
                for _ in range(n):
                    val = int(next(it))
                    tail.next = Node(val)
                    tail = tail.next
                arr.append(dummy.next)
            sol = Solution()
            merged_head = sol.mergeKLists(arr)
            print_list(merged_head)