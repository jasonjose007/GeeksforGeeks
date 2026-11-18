# XOR of Number Range
# Platform: GFG
# Difficulty: Easy
# Topics: Bit Magic

import sys


def xor_upto(n):
    rem = n & 3
    if rem == 0:
        return n
    if rem == 1:
        return 1
    if rem == 2:
        return n + 1
    return 0


def main():
    data = sys.stdin.read().split()
    if len(data) >= 2:
        l = int(data[0])
        r = int(data[1])
        print(xor_upto(r) ^ xor_upto(l - 1))


if __name__ == "__main__":
    main()