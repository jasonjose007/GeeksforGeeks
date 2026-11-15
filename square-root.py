# Square Root
# Platform: GFG
# Difficulty: Easy
# Topics: Searching, Mathematics, Binary Search

def floor_sqrt(n):
    if n < 2:
        return n
    low, high = 1, n // 2
    ans = 1
    while low <= high:
        mid = (low + high) // 2
        sq = mid * mid
        if sq == n:
            return mid
        elif sq < n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

n = int(input().strip())
print(floor_sqrt(n))