# Median in Stream
# Platform: GFG
# Difficulty: Medium
# Topics: Heap, Design-Pattern, Sorting

import heapq


def get_median(arr):
    low = []
    high = []
    res = []
    for x in arr:
        heapq.heappush(low, -x)
        heapq.heappush(high, -heapq.heappop(low))
        if len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))
        if len(low) > len(high):
            res.append(float(-low[0]))
        else:
            res.append((-low[0] + high[0]) / 2.0)
    return res


def solve():
    lines = []
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if line:
            cleaned = line.replace("[", " ").replace("]", " ").replace(",", " ")
            nums = [int(tok) for tok in cleaned.split()]
            if nums:
                lines.append(nums)

    if not lines:
        return

    if len(lines) >= 2 and len(lines[0]) == 1 and lines[0][0] == sum(len(row) for row in lines[1:]):
        arr = [val for row in lines[1:] for val in row]
    else:
        arr = [val for row in lines for val in row]

    ans = get_median(arr)
    print(" ".join(str(x) for x in ans))


if __name__ == "__main__":
    solve()