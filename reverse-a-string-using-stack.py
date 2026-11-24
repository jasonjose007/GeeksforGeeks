# Reverse Using Stack
# Platform: GFG
# Difficulty: Easy
# Topics: Strings, Stack, Data Structures

s = input()
stack = []
for ch in s:
    stack.append(ch)
res = []
while stack:
    res.append(stack.pop())
print("".join(res))