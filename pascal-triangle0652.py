# Pascal Triangle
# Platform: GFG
# Difficulty: Medium
# Topics: Arrays, Recursion

n = int(input().strip())
row = [1]
val = 1
for k in range(1, n):
    val = val * (n - k) // k
    row.append(val)
print(*row)