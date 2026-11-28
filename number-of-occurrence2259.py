# Count Occurrences in Sorted
# Platform: GFG
# Difficulty: Medium
# Topics: Arrays, Searching

from bisect import bisect_left, bisect_right


def parse_nums(s):
    s = s.replace("[", " ").replace("]", " ").replace(",", " ")
    return [int(x) for x in s.split()]


def main():
    lines = []
    while True:
        try:
            line = input().strip()
            if line:
                lines.append(line)
        except EOFError:
            break

    if not lines:
        return

    if len(lines) == 1:
        p0 = parse_nums(lines[0])
        arr, target = p0[:-1], p0[-1]
    elif len(lines) == 2:
        p0 = parse_nums(lines[0])
        p1 = parse_nums(lines[1])
        if len(p0) == 2 and len(p1) == p0[0] and len(p1) > 1:
            arr, target = p1, p0[1]
        else:
            arr, target = p0, p1[0]
    elif len(lines) == 3:
        arr = parse_nums(lines[1])
        target = parse_nums(lines[2])[0]
    else:
        tc = parse_nums(lines[0])[0]
        idx = 1
        out = []
        for _ in range(tc):
            p = parse_nums(lines[idx])
            if len(p) == 1 and idx + 2 < len(lines):
                arr = parse_nums(lines[idx + 1])
                target = parse_nums(lines[idx + 2])[0]
                idx += 3
            else:
                arr = p
                target = parse_nums(lines[idx + 1])[0]
                idx += 2
            out.append(str(bisect_right(arr, target) - bisect_left(arr, target)))
        print("\n".join(out))
        return

    print(bisect_right(arr, target) - bisect_left(arr, target))


if __name__ == "__main__":
    main()