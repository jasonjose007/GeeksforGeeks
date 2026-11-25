# Palindrome Sentence
# Platform: GFG
# Difficulty: Easy
# Topics: two-pointer-algorithm, Strings, palindrome

import sys

def main():
    s = sys.stdin.read()
    s_lower = s.lower()
    filtered = [ch for ch in s_lower if ch.isalnum()]
    if filtered == filtered[::-1]:
        print("true")
    else:
        print("false")

if __name__ == '__main__':
    main()