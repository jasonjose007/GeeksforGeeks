# Repeated Pattern Check
# Platform: GFG
# Difficulty: Easy
# Topics: Strings

import sys


def is_valid(s):
    n = len(s)
    if n == 0:
        return False
    i = 0
    while i < n:
        cx = 0
        while i < n and s[i] == "x":
            cx += 1
            i += 1
        if cx == 0:
            return False
        cy = 0
        while i < n and s[i] == "y":
            cy += 1
            i += 1
        if cx != cy:
            return False
    return True


def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    if tokens[0].isdigit():
        t = int(tokens[0])
        for i in range(1, t + 1):
            if i < len(tokens):
                s = tokens[i].strip("\"'")
                print("true" if is_valid(s) else "false")
    else:
        for token in tokens:
            s = token.strip("\"'")
            print("true" if is_valid(s) else "false")


if __name__ == "__main__":
    main()