# Count Graphs with n Vertices
# Platform: GFG
# Difficulty: Easy
# Topics: Graph, Mathematics, Bit Magic

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    for item in input_data:
        n = int(item)
        edges = n * (n - 1) // 2
        print(2 ** edges)

if __name__ == '__main__':
    main()