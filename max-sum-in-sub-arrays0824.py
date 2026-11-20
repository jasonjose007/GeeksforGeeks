# Max Sum of 2 Smallest Across Subarrays
# Platform: GFG
# Difficulty: Medium
# Topics: Arrays, Stack

def solve():
    first = input().replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
    if len(first) == 1:
        n = int(first[0])
        arr = []
        while len(arr) < n:
            arr.extend(map(int, input().replace('[', ' ').replace(']', ' ').replace(',', ' ').split()))
    else:
        arr = list(map(int, first))

    ans = arr[0] + arr[1]
    for i in range(1, len(arr) - 1):
        s = arr[i] + arr[i + 1]
        if s > ans:
            ans = s
    print(ans)

if __name__ == "__main__":
    solve()