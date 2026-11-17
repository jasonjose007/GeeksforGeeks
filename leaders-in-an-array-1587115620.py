# Array Leaders
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays

import sys


def main():
    raw_input = sys.stdin.read().strip()
    if not raw_input:
        return

    tokens = raw_input.split()
    if not tokens:
        return

    def process_array(arr):
        leaders = []
        max_right = -1
        for x in reversed(arr):
            if x >= max_right:
                leaders.append(x)
                max_right = x
        leaders.reverse()
        print(*leaders)

    try:
        T = int(tokens[0])
        idx = 1
        test_cases = []
        possible = True
        for _ in range(T):
            if idx >= len(tokens):
                possible = False
                break
            N = int(tokens[idx])
            idx += 1
            if idx + N > len(tokens):
                possible = False
                break
            arr = [int(x) for x in tokens[idx : idx + N]]
            idx += N
            test_cases.append(arr)
        if possible and idx == len(tokens) and T > 0:
            for arr in test_cases:
                process_array(arr)
            return
    except ValueError:
        pass

    try:
        N = int(tokens[0])
        if N > 0 and N == len(tokens) - 1:
            arr = [int(x) for x in tokens[1:]]
            process_array(arr)
            return
    except ValueError:
        pass

    lines = raw_input.splitlines()
    non_empty_lines = [l.strip() for l in lines if l.strip()]

    if len(non_empty_lines) > 1:
        for line in non_empty_lines:
            arr = [int(x) for x in line.split()]
            process_array(arr)
    else:
        arr = [int(x) for x in tokens]
        process_array(arr)


if __name__ == "__main__":
    main()