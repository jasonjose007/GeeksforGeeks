# Panagram Checking
# Platform: GFG
# Difficulty: Easy
# Topics: Strings

import sys

def main():
    s = sys.stdin.read()
    letters = set()
    for ch in s.lower():
        if 'a' <= ch <= 'z':
            letters.add(ch)
            if len(letters) == 26:
                print("true")
                return
    print("false")

if __name__ == '__main__':
    main()