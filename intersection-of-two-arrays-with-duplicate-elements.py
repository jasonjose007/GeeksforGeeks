# Intersection of Two arrays with Duplicate Elements
# Platform: GFG
# Difficulty: Easy
# Topics: Sorting, two-pointer-algorithm, Arrays, Hash

def parse_line(s):
    s = s.replace("[", " ").replace("]", " ").replace(",", " ")
    return list(map(int, s.split()))

def read_all_lines():
    lines = []
    while True:
        try:
            line = input().strip()
            if line:
                lines.append(line)
        except EOFError:
            break
    return lines

def solve():
    raw_lines = read_all_lines()
    if not raw_lines:
        return
    parsed = [parse_line(line) for line in raw_lines]

    cases = []
    if len(parsed) == 2:
        cases.append((parsed[0], parsed[1]))
    elif len(parsed) == 3 and len(parsed[0]) == 2 and parsed[0][0] == len(parsed[1]) and parsed[0][1] == len(parsed[2]):
        cases.append((parsed[1], parsed[2]))
    elif len(parsed) == 4 and len(parsed[0]) == 1 and len(parsed[2]) == 1 and parsed[0][0] == len(parsed[1]) and parsed[2][0] == len(parsed[3]):
        cases.append((parsed[1], parsed[3]))
    elif len(parsed[0]) == 1 and len(parsed) > 2:
        t = parsed[0][0]
        idx = 1
        for _ in range(t):
            if idx + 1 >= len(parsed):
                break
            if idx + 3 < len(parsed) and len(parsed[idx]) == 1 and len(parsed[idx + 2]) == 1 and parsed[idx][0] == len(parsed[idx + 1]) and parsed[idx + 2][0] == len(parsed[idx + 3]):
                cases.append((parsed[idx + 1], parsed[idx + 3]))
                idx += 4
            elif idx + 2 < len(parsed) and len(parsed[idx]) == 2 and parsed[idx][0] == len(parsed[idx + 1]) and parsed[idx][1] == len(parsed[idx + 2]):
                cases.append((parsed[idx + 1], parsed[idx + 2]))
                idx += 3
            else:
                cases.append((parsed[idx], parsed[idx + 1]))
                idx += 2
    else:
        for i in range(0, len(parsed) - 1, 2):
            cases.append((parsed[i], parsed[i + 1]))

    for a, b in cases:
        if len(a) > len(b):
            a, b = b, a
        seen = set(a)
        res = sorted({x for x in b if x in seen})
        if res:
            print(" ".join(map(str, res)))
        else:
            print("[]")

solve()