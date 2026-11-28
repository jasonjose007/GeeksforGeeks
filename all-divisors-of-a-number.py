# All Divisors of Number
# Platform: GFG
# Difficulty: Easy
# Topics: Mathematics, Factorization

import math

n = int(input().strip())
small = []
large = []

for i in range(1, math.isqrt(n) + 1):
    if n % i == 0:
        small.append(i)
        if i != n // i:
            large.append(n // i)

print(*(small + large[::-1]))