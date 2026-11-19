# Missing And Repeating
# Platform: GFG
# Difficulty: Easy
# Topics: Bit Magic

def solve(arr):
    n = len(arr)
    s_exp = n * (n + 1) // 2
    s2_exp = n * (n + 1) * (2 * n + 1) // 6
    s = 0
    s2 = 0
    for x in arr:
        s += x
        s2 += x * x
    diff = s - s_exp
    diff2 = s2 - s2_exp
    sum_rm = diff2 // diff
    r = (diff + sum_rm) // 2
    m = sum_rm - r
    return r, m


def main():
    parsed = []
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if not line:
            continue
        nums = [
            int(tok)
            for tok in line.replace("[", " ").replace("]", " ").replace(",", " ").split()
        ]
        if nums:
            parsed.append(nums)

    if not parsed:
        return

    cases = []
    if len(parsed) == 1:
        cases = [parsed[0]]
    elif len(parsed) == 2:
        if len(parsed[0]) == 1:
            cases = [parsed[1]]
        else:
            cases = parsed
    else:
        if len(parsed[0]) == 1:
            first = parsed[0][0]
            if first == len(parsed) - 1 and all(len(x) == 1 for x in parsed[1:]):
                cases = [[x[0] for x in parsed[1:]]]
            else:
                t = first
                rem = parsed[1:]
                if len(rem) == 2 * t:
                    cases = [rem[2 * i + 1] for i in range(t)]
                elif len(rem) == t:
                    cases = rem
                else:
                    idx = 0
                    while idx < len(rem) and len(cases) < t:
                        if len(rem[idx]) == 1 and idx + 1 < len(rem):
                            n_val = rem[idx][0]
                            arr = []
                            idx += 1
                            while len(arr) < n_val and idx < len(rem):
                                arr.extend(rem[idx])
                                idx += 1
                            cases.append(arr)
                        else:
                            cases.append(rem[idx])
                            idx += 1
        else:
            cases = parsed

    for arr in cases:
        r, m = solve(arr)
        print(r, m)


if __name__ == "__main__":
    main()