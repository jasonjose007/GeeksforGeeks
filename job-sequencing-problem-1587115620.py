# Job Sequencing Problem
# Platform: GFG
# Difficulty: Medium
# Topics: Greedy, Disjoint Set

import heapq

def solve():
    lines = []
    while True:
        try:
            line = input()
        except (EOFError, StopIteration):
            break
        cleaned = line.replace('[', ' ').replace(']', ' ').replace(',', ' ').strip()
        if cleaned:
            lines.append(list(map(int, cleaned.split())))

    if not lines:
        return

    if len(lines) == 2 and len(lines[0]) == len(lines[1]):
        deadline, profit = lines[0], lines[1]
    elif len(lines) == 3 and len(lines[0]) == 1 and len(lines[1]) == lines[0][0] and len(lines[2]) == lines[0][0]:
        deadline, profit = lines[1], lines[2]
    else:
        nums = [x for row in lines for x in row]
        if len(nums) % 2 == 1 and len(nums) == 2 * nums[0] + 1:
            n = nums[0]
            deadline = nums[1:1 + n]
            profit = nums[1 + n:]
        else:
            n = len(nums) // 2
            deadline = nums[:n]
            profit = nums[n:]

    pq = []
    for d, p in sorted(zip(deadline, profit)):
        if len(pq) < d:
            heapq.heappush(pq, p)
        elif pq and pq[0] < p:
            heapq.heapreplace(pq, p)

    print(len(pq), sum(pq))

if __name__ == "__main__":
    solve()