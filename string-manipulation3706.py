# Remove Two Consecutive Same
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, Stack

import sys


def main():
    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    if not lines:
        return

    if len(lines) == 1:
        tokens = lines[0].split()
        if tokens[0].isdigit() and int(tokens[0]) == len(tokens) - 1:
            arr = tokens[1:]
        else:
            arr = tokens
    elif len(lines) == 2:
        tokens1 = lines[0].split()
        tokens2 = lines[1].split()
        if len(tokens1) == 1 and tokens1[0].isdigit():
            arr = tokens2
        else:
            arr = tokens1 + tokens2
    else:
        all_tokens = []
        for line in lines:
            all_tokens.extend(line.split())
        if all_tokens and all_tokens[0].isdigit() and int(all_tokens[0]) == len(all_tokens) - 1:
            arr = all_tokens[1:]
        else:
            arr = all_tokens

    stack = []
    for word in arr:
        if stack and stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)

    print(len(stack))


if __name__ == "__main__":
    main()