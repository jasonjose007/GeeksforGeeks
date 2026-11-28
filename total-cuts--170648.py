# Total Cuts
# Platform: GFG
# Difficulty: Easy
# Topics: Prefix Sum, Arrays

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

    parsed = [
        list(map(int, l.replace('[', ' ').replace(']', ' ').replace(',', ' ').split()))
        for l in lines
    ]

    a = []
    k = 0

    if len(parsed) == 3:
        if len(parsed[0]) == 1 and len(parsed[1]) == 1 and len(parsed[2]) == parsed[0][0]:
            k = parsed[1][0]
            a = parsed[2]
        elif len(parsed[0]) == 1 and len(parsed[2]) == 1 and len(parsed[1]) == parsed[0][0]:
            a = parsed[1]
            k = parsed[2][0]
        else:
            a = parsed[1]
            k = parsed[2][0]
    elif len(parsed) == 2:
        if len(parsed[0]) == 2 and len(parsed[1]) == parsed[0][0] and not (parsed[0][0] == 1 and len(parsed[1]) == 1):
            k = parsed[0][1]
            a = parsed[1]
        elif len(parsed[1]) == 1 and len(parsed[0]) >= 2:
            a = parsed[0]
            k = parsed[1][0]
        elif len(parsed[0]) == 1 and len(parsed[1]) == 1:
            print(0)
            return
        else:
            k = parsed[0][1]
            a = parsed[1]
    else:
        nums = parsed[0]
        if len(nums) >= 3 and nums[0] == len(nums) - 2:
            k = nums[1]
            a = nums[2:]
        else:
            a = nums[:-1]
            k = nums[-1]

    n = len(a)
    if n <= 1:
        print(0)
        return

    suff_min = [0] * n
    cur_min = a[-1]
    for i in range(n - 1, -1, -1):
        val = a[i]
        if val < cur_min:
            cur_min = val
        suff_min[i] = cur_min

    ans = 0
    cur_max = a[0]
    for i in range(n - 1):
        val = a[i]
        if val > cur_max:
            cur_max = val
        if cur_max + suff_min[i + 1] >= k:
            ans += 1

    print(ans)


solve()