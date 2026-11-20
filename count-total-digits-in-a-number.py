# Count Digits in Number
# Platform: GFG
# Difficulty: Easy
# Topics: Recursion

s = input().strip()
if s.startswith('-'):
    s = s[1:]
s = s.lstrip('0')
print(len(s) if s else 1)