# Move all Negatives to End
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays

def segregate_elements(arr):
    arr[:] = [x for x in arr if x >= 0] + [x for x in arr if x < 0]


def parse_ints(line):
    return list(map(int, line.replace("[", " ").replace("]", " ").replace(",", " ").split()))


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
        arr = parsed[0]
        segregate_elements(arr)
        print(*arr)
    elif len(parsed) == 2 and len(parsed[0]) == 1 and parsed[0][0] == len(parsed[1]):
        arr = parsed[1]
        segregate_elements(arr)
        print(*arr)
    elif len(parsed[0]) == 1 and len(parsed) == 1 + 2 * parsed[0][0]:
        t = parsed[0][0]
        for i in range(t):
            arr = parsed[2 + 2 * i]
            segregate_elements(arr)
            print(*arr)
    elif len(parsed[0]) == 1 and len(parsed) == 1 + parsed[0][0]:
        t = parsed[0][0]
        for i in range(t):
            arr = parsed[1 + i]
            segregate_elements(arr)
            print(*arr)
    else:
        for arr in parsed:
            segregate_elements(arr)
            print(*arr)


if __name__ == "__main__":
    main()