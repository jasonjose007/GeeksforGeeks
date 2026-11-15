# Recursive Sequence
# Platform: GFG
# Difficulty: Easy
# Topics: Mathematics, Recursion

def main():
    n = int(input().strip())
    mod = 10**9 + 7
    ans = 0
    curr = 1
    for i in range(1, n + 1):
        prod = 1
        for _ in range(i):
            prod = (prod * curr) % mod
            curr += 1
        ans = (ans + prod) % mod
    print(ans)

if __name__ == "__main__":
    main()