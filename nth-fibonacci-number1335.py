# Nth Fibonacci Number
# Platform: GFG
# Difficulty: Easy
# Topics: Fibonacci, Mathematics

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    
    if n == 0:
        print(0)
        return
    if n == 1:
        print(1)
        return
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(b)

if __name__ == '__main__':
    main()