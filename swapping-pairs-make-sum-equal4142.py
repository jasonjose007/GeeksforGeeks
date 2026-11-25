# Swap Pairs Make Sum Equal
# Platform: GFG
# Difficulty: Medium
# Topics: Arrays, Hash

import sys


def solve_one(a, b):
    sum_a = sum(a)
    sum_b = sum(b)

    diff = sum_a - sum_b
    if diff % 2 != 0:
        return "false"

    target = diff // 2
    set_a = set(a)

    for y in b:
        if (y + target) in set_a:
            return "true"

    return "false"


def main():
    raw_data = sys.stdin.read().strip()
    if not raw_data:
        return

    lines = [line.strip() for line in raw_data.split("\n") if line.strip()]

    def parse_line(l):
        l = l.replace("[", "").replace("]", "").replace(",", " ")
        return [int(x) for x in l.split()]

    parsed_lines = [parse_line(l) for l in lines]
    num_lines = len(parsed_lines)

    if num_lines == 2:
        print(solve_one(parsed_lines[0], parsed_lines[1]))
        return
    elif num_lines == 3 and len(parsed_lines[0]) <= 2:
        print(solve_one(parsed_lines[1], parsed_lines[2]))
        return
    elif num_lines == 4:
        print(solve_one(parsed_lines[1], parsed_lines[3]))
        return

    i = 0
    if len(parsed_lines[0]) == 1 and (num_lines - 1) % 2 == 0:
        i = 1
    elif len(parsed_lines[0]) == 1 and (num_lines - 1) % 3 == 0:
        i = 1

    while i < num_lines:
        if len(parsed_lines[i]) <= 2 and i + 2 < num_lines:
            if len(parsed_lines[i]) == 2:
                print(solve_one(parsed_lines[i + 1], parsed_lines[i + 2]))
                i += 3
                continue
            elif (
                len(parsed_lines[i]) == 1
                and i + 3 < num_lines
                and len(parsed_lines[i + 2]) == 1
            ):
                print(solve_one(parsed_lines[i + 1], parsed_lines[i + 3]))
                i += 4
                continue

        if i + 1 < num_lines:
            print(solve_one(parsed_lines[i], parsed_lines[i + 1]))
            i += 2
        else:
            break


if __name__ == "__main__":
    main()