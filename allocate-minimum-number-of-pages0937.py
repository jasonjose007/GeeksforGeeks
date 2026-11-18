# Allocate Minimum Pages
# Platform: GFG
# Difficulty: Medium
# Topics: Searching, Divide and Conquer

def allocate_min_pages(arr, k):
    n = len(arr)
    if k <= 0 or n < k:
        return -1

    low = max(arr)
    high = sum(arr)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        students = 1
        current_pages = 0
        for pages in arr:
            if current_pages + pages > mid:
                students += 1
                current_pages = pages
                if students > k:
                    break
            else:
                current_pages += pages

        if students <= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def parse_ints(line):
    cleaned = line.replace('[', ' ').replace(']', ' ').replace(',', ' ')
    return list(map(int, cleaned.split()))


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

    parsed = [parse_ints(line) for line in lines]

    if len(parsed) == 1:
        tokens = parsed[0]
        if len(tokens) >= 2:
            print(allocate_min_pages(tokens[:-1], tokens[-1]))
    elif len(parsed) == 2:
        t0, t1 = parsed[0], parsed[1]
        if len(t0) == 2 and len(t1) == t0[0] and len(t1) > 1:
            print(allocate_min_pages(t1, t0[1]))
        else:
            print(allocate_min_pages(t0, t1[0]))
    elif len(parsed) == 3 and len(parsed[0]) == 1 and len(parsed[2]) == 1:
        print(allocate_min_pages(parsed[1], parsed[2][0]))
    elif len(parsed[0]) == 1 and len(parsed) == 1 + 3 * parsed[0][0]:
        t = parsed[0][0]
        idx = 1
        for _ in range(t):
            arr = parsed[idx + 1]
            k = parsed[idx + 2][0]
            print(allocate_min_pages(arr, k))
            idx += 3
    elif len(parsed[0]) == 1 and len(parsed) == 1 + 2 * parsed[0][0]:
        t = parsed[0][0]
        idx = 1
        for _ in range(t):
            t0, t1 = parsed[idx], parsed[idx + 1]
            if len(t0) == 2 and len(t1) == t0[0] and len(t1) > 1:
                print(allocate_min_pages(t1, t0[1]))
            else:
                print(allocate_min_pages(t0, t1[0]))
            idx += 2
    else:
        tokens = [x for row in parsed for x in row]
        if len(tokens) >= 2:
            print(allocate_min_pages(tokens[:-1], tokens[-1]))


if __name__ == "__main__":
    main()