# Delete Smaller Than Next
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, Stack

def solve():
    def parse_nums(s):
        return list(map(int, s.replace('[', ' ').replace(']', ' ').replace(',', ' ').split()))

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
        nums = parse_nums(lines[0])
        arr = nums[:-1]
        k = nums[-1]
    elif len(lines) == 2:
        p1 = parse_nums(lines[0])
        p2 = parse_nums(lines[1])
        if len(p2) == 1:
            arr = p1
            k = p2[0]
        else:
            k = p1[-1]
            arr = p2
    else:
        arr = parse_nums(lines[1])
        k = parse_nums(lines[2])[0]

    st = []
    for x in arr:
        while st and k > 0 and st[-1] < x:
            st.pop()
            k -= 1
        st.append(x)

    print(*st)


if __name__ == "__main__":
    solve()