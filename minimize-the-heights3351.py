# Minimize the Heights
# Platform: GFG
# Difficulty: Medium
# Topics: Arrays, Greedy

def parse_ints(line):
    return list(map(int, line.replace(',', ' ').replace('[', ' ').replace(']', ' ').split()))


def solve():
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

    parsed = [parse_ints(line) for line in lines]

    if len(parsed) == 1:
        k = parsed[0][0]
        arr = parsed[0][1:]
    elif len(parsed) == 2:
        l0, l1 = parsed
        if len(l0) == 1:
            k = l0[0]
            arr = l1
        elif len(l1) == 1:
            arr = l0
            k = l1[0]
        elif len(l0) == 2 and len(l1) == l0[0]:
            k = l0[1]
            arr = l1
        else:
            k = l0[0]
            arr = l1
    else:
        l0, l1, l2 = parsed[0], parsed[1], parsed[2]
        if len(l0) == 1 and len(l1) == 1:
            if len(l2) == l1[0]:
                k = l0[0]
                arr = l2
            elif len(l2) == l0[0]:
                k = l1[0]
                arr = l2
            else:
                k = l0[0]
                arr = l2
        else:
            k = l0[0]
            arr = l1

    n = len(arr)
    if n <= 1:
        print(0)
        return

    arr.sort()
    ans = arr[-1] - arr[0]

    for i in range(1, n):
        if arr[i] - k < 0:
            continue
        mini = min(arr[0] + k, arr[i] - k)
        maxi = max(arr[i - 1] + k, arr[-1] - k)
        diff = maxi - mini
        if diff < ans:
            ans = diff

    print(ans)


if __name__ == "__main__":
    solve()