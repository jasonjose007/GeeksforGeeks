# Sum of Dependencies in Graph
# Platform: GFG
# Difficulty: Easy
# Topics: Graph

def main():
    tokens = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line:
            tokens.extend(line.split())
    if not tokens:
        return
    if len(tokens) == 2 + 2 * int(tokens[1]):
        print(int(tokens[1]))
    else:
        t = int(tokens[0])
        idx = 1
        for _ in range(t):
            e = int(tokens[idx + 1])
            print(e)
            idx += 2 + 2 * e

main()