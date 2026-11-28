# Implementation of Priority Queue using Binary Heap
# Platform: GFG
# Difficulty: Easy
# Topics: Heap

import sys


def main():
    lines = sys.stdin.read().splitlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        arr = list(map(int, line.split()))
        if not arr:
            continue

        heap = []
        for val in arr:
            heap.append(val)
            curr = len(heap) - 1
            while curr > 0:
                parent = (curr - 1) // 2
                if heap[curr] > heap[parent]:
                    heap[curr], heap[parent] = heap[parent], heap[curr]
                    curr = parent
                else:
                    break

        if not heap:
            continue

        max_val = heap[0]
        heap[0] = heap[-1]
        heap.pop()

        curr = 0
        n = len(heap)
        while True:
            left = 2 * curr + 1
            right = 2 * curr + 2
            largest = curr
            if left < n and heap[left] > heap[largest]:
                largest = left
            if right < n and heap[right] > heap[largest]:
                largest = right
            if largest != curr:
                heap[curr], heap[largest] = heap[largest], heap[curr]
                curr = largest
            else:
                break

        print(max_val)
        if heap:
            print(
                "Priority Queue after extracting maximum: "
                + " ".join(map(str, heap))
            )
        else:
            print("Priority Queue after extracting maximum:")


if __name__ == "__main__":
    main()