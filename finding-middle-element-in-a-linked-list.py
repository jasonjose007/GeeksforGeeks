# Middle of Linked List
# Platform: GFG
# Difficulty: Easy
# Topics: Linked List, two-pointer-algorithm

import sys

def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return

    is_t = False
    try:
        first_val = int(lines[0])
        is_t = True
    except ValueError:
        is_t = False

    if is_t:
        t = first_val
        rem = lines[1:]
        if len(rem) == t:
            for line in rem:
                arr = list(map(int, line.split()))
                print(arr[len(arr) // 2])
            return
        elif len(rem) == 2 * t:
            for i in range(t):
                arr = list(map(int, rem[2 * i + 1].split()))
                print(arr[len(arr) // 2])
            return

    for line in lines:
        arr = list(map(int, line.split()))
        print(arr[len(arr) // 2])

if __name__ == "__main__":
    main()