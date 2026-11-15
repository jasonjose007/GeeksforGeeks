# Sum of All Digit Subsequences
# Platform: GFG
# Difficulty: Easy
# Topics: Strings

def solve():
    try:
        s = input().strip()
    except EOFError:
        s = ""
    if not s:
        print(0)
        return
    MOD = 10**9 + 7
    digit_sum = sum(ord(c) - 48 for c in s)
    ans = (digit_sum * pow(2, len(s) - 1, MOD)) % MOD
    print(ans)

if __name__ == "__main__":
    solve()