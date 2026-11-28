# Most Frequent Character
# Platform: GFG
# Difficulty: Easy
# Topics: Strings

def solve():
    s = input().strip()
    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - 97] += 1
    max_freq = -1
    ans = ""
    for i in range(26):
        if freq[i] > max_freq:
            max_freq = freq[i]
            ans = chr(i + 97)
    print(ans)


if __name__ == "__main__":
    solve()