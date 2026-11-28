# Prime Number
# Platform: GFG
# Difficulty: Easy
# Topics: Mathematics, Prime Number

import sys


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        if is_prime(n):
            print("true")
        else:
            print("false")


if __name__ == "__main__":
    main()