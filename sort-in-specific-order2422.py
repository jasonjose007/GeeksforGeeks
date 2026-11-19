# Sort in Specific Order
# Platform: GFG
# Difficulty: Medium
# Topics: Arrays, Sorting, Numbers

import sys

def parse_ints(s):
    return list(map(int, s.replace('[', ' ').replace(']', ' ').replace(',', ' ').split()))

def solve_arr(arr):
    odds = [x for x in arr if x & 1]
    evens = [x for x in arr if not (x & 1)]
    odds.sort(reverse=True)
    evens.sort()
    return odds + evens

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if len(lines) == 1:
        print(*solve_arr(parse_ints(lines[0])))
    elif len(lines) == 2 and len(parse_ints(lines[0])) == 1:
        print(*solve_arr(parse_ints(lines[1])))
    elif len(lines) > 2 and len(parse_ints(lines[0])) == 1:
        t = parse_ints(lines[0])[0]
        if len(lines) == 1 + t:
            for line in lines[1:]:
                print(*solve_arr(parse_ints(line)))
        elif len(lines) == 1 + 2 * t:
            for i in range(1, len(lines), 2):
                print(*solve_arr(parse_ints(lines[i + 1])))
        else:
            tokens = parse_ints(data)
            if tokens and tokens[0] == len(tokens) - 1:
                tokens = tokens[1:]
            print(*solve_arr(tokens))
    else:
        tokens = parse_ints(data)
        print(*solve_arr(tokens))

if __name__ == "__main__":
    main()