# Reverse Words
# Platform: GFG
# Difficulty: Easy
# Topics: Strings

import sys

def main():
    input_data = sys.stdin.read().split()
    if input_data:
        s = input_data[0]
        words = [w for w in s.split('.') if w]
        print('.'.join(reversed(words)))

if __name__ == '__main__':
    main()