# At Least K Occurrences
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, Hash

import sys


def solve_case(arr, k):
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] == k:
            return num
    return -1


def main():
    input_text = sys.stdin.read().strip()
    if not input_text:
        return

    lines = [line.strip() for line in input_text.splitlines() if line.strip()]

    if len(lines) == 2:
        parts0 = list(map(int, lines[0].split()))
        parts1 = list(map(int, lines[1].split()))

        if len(parts1) == 1 and len(parts0) != 2:
            arr = parts0
            k = parts1[0]
        elif len(parts0) == 2:
            n, k = parts0
            arr = parts1
        elif len(parts1) == 1:
            arr = parts0
            k = parts1[0]
        else:
            all_tokens = parts0 + parts1
            arr = all_tokens[:-1]
            k = all_tokens[-1]
        print(solve_case(arr, k))
        return

    if len(lines) == 1:
        tokens = list(map(int, lines[0].split()))
        if len(tokens) >= 3 and tokens[0] == len(tokens) - 2:
            k = tokens[1]
            arr = tokens[2:]
        else:
            arr = tokens[:-1]
            k = tokens[-1]
        print(solve_case(arr, k))
        return

    tokens_first = list(map(int, lines[0].split()))
    if len(tokens_first) == 1:
        t = tokens_first[0]
        curr = 1
        for _ in range(t):
            if curr >= len(lines):
                break
            p1 = list(map(int, lines[curr].split()))
            if curr + 1 < len(lines):
                p2 = list(map(int, lines[curr + 1].split()))
                if len(p2) == 1:
                    arr = p1
                    k = p2[0]
                    curr += 2
                elif len(p1) == 2:
                    k = p1[1]
                    arr = p2
                    curr += 2
                else:
                    arr = p1[:-1]
                    k = p1[-1]
                    curr += 1
            else:
                arr = p1[:-1]
                k = p1[-1]
                curr += 1
            print(solve_case(arr, k))
    else:
        all_tokens = []
        for line in lines:
            all_tokens.extend(list(map(int, line.split())))
        arr = all_tokens[:-1]
        k = all_tokens[-1]
        print(solve_case(arr, k))


if __name__ == "__main__":
    main()