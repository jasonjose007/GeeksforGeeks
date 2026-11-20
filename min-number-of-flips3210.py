# Min Flips for Alternate
# Platform: GFG
# Difficulty: Easy
# Topics: Strings, Binary Representation

s = input().strip()
flips = 0
for i, c in enumerate(s):
    if c != ('1' if i & 1 else '0'):
        flips += 1
print(min(flips, len(s) - flips))