# Nearest Multiple of 10
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, Strings, Mathematics

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    for s in input_data:
        if int(s[-1]) <= 5:
            print(s[:-1] + "0")
        else:
            prefix = list(s[:-1])
            i = len(prefix) - 1
            carry = 1
            while i >= 0 and carry:
                if prefix[i] == "9":
                    prefix[i] = "0"
                else:
                    prefix[i] = str(int(prefix[i]) + 1)
                    carry = 0
                i -= 1
            if carry:
                print("1" + "".join(prefix) + "0")
            else:
                print("".join(prefix) + "0")


if __name__ == "__main__":
    solve()