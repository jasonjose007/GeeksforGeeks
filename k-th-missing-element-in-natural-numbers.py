# K-th Missing in Natural Numbers
# Platform: GFG
# Difficulty: Medium
# Topics: Arrays, Sorting

import re
import sys


def kth_missing(arr, k):
    arr.sort()
    for x in arr:
        if x <= k:
            k += 1
        else:
            break
    return k


def main():
    input_text = sys.stdin.read().strip()
    if not input_text:
        return

    lines = [line.strip() for line in input_text.splitlines() if line.strip()]
    parsed_lines = []
    for line in lines:
        nums = [int(x) for x in re.findall(r"-?\d+", line)]
        if nums:
            parsed_lines.append(nums)

    if not parsed_lines:
        return

    if len(parsed_lines) == 1:
        nums = parsed_lines[0]
        arr = nums[:-1]
        k = nums[-1]
        print(kth_missing(arr, k))
        return

    idx = 0
    if len(parsed_lines[0]) == 1 and (len(parsed_lines) - 1) % 2 == 0:
        idx = 1

    while idx < len(parsed_lines):
        if idx + 1 < len(parsed_lines):
            line1 = parsed_lines[idx]
            line2 = parsed_lines[idx + 1]

            if len(line1) == 2 and len(line2) > 1:
                k = line1[1]
                arr = line2
            elif len(line1) > 1 and len(line2) == 1:
                arr = line1
                k = line2[0]
            elif len(line1) == 1 and len(line2) > 1:
                if (
                    idx + 2 < len(parsed_lines)
                    and len(parsed_lines[idx + 2]) == 1
                ):
                    arr = line2
                    k = parsed_lines[idx + 2][0]
                    idx += 1
                else:
                    arr = line2
                    k = line1[0]
            else:
                arr = line1
                k = line2[0]

            print(kth_missing(arr, k))
            idx += 2
        else:
            break


if __name__ == "__main__":
    main()