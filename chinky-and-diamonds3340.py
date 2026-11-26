# Maximum Diamonds
# Platform: GFG
# Difficulty: Easy
# Topics: Mathematics, STL, Heap

import sys
import heapq

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    # Filter out empty lines
    lines = [line.strip() for line in lines if line.strip()]
    
    # Check if first line is number of test cases
    line_idx = 0
    
    def parse_ints(s):
        # handles both space-separated and [1, 2, 3] format
        s = s.replace('[', ' ').replace(']', ' ').replace(',', ' ')
        return [int(x) for x in s.split()]

    first_tokens = parse_ints(lines[0])
    
    # Determine structure
    # Possibility A: T test cases
    # Possibility B: stream of tokens
    tokens = []
    for line in lines:
        tokens.extend(parse_ints(line))
        
    if not tokens:
        return

    # Let's inspect tokens.
    # Often GFG has:
    # T
    # N K
    # arr of N ints
    # OR:
    # arr
    # k
    # Let's write a flexible runner or detect format:
    # If the first token is T, and matches remaining test cases.
    # What if it's N, K, then arr?
    # What if arr then k?
    # Notice: if it's arr then k:
    # line 1: arr
    # line 2: k
    # If there are 2 lines or 2*T lines:
    
    # Let's check line by line:
    # If line 0 has 1 element T, and remaining lines == 2*T:
    # Each testcase is 2 lines: arr and k, or (N, K) and arr.
    if len(first_tokens) == 1 and len(lines) == 1 + 2 * first_tokens[0]:
        T = first_tokens[0]
        idx = 1
        for _ in range(T):
            l1 = parse_ints(lines[idx])
            l2 = parse_ints(lines[idx+1])
            idx += 2
            if len(l1) == 2 and len(l2) == l1[0]:
                # N, K then arr
                n, k = l1
                arr = l2
            elif len(l2) == 1:
                # arr then k
                arr = l1
                k = l2[0]
            else:
                # fallback
                arr = l1
                k = l2[0] if l2 else 0
            ans = get_max_diamonds(arr, k)
            print(ans)
        return

    # If len(lines) == 2:
    if len(lines) == 2:
        l1 = parse_ints(lines[0])
        l2 = parse_ints(lines[1])
        if len(l1) == 2 and len(l2) == l1[0]:
            print(get_max_diamonds(l2, l1[1]))
            return
        elif len(l2) == 1:
            print(get_max_diamonds(l1, l2[0]))
            return

    # Otherwise, check if tokens start with T and (N, K, arr) pattern:
    # Let's check token-based:
    T = tokens[0]
    # Try parsing as T test cases of N, K, arr
    curr = 1
    possible = True
    test_cases = []
    while curr < len(tokens):
        if curr + 1 >= len(tokens):
            possible = False
            break
        n = tokens[curr]
        k = tokens[curr+1]
        curr += 2
        if curr + n > len(tokens):
            possible = False
            break
        arr = tokens[curr:curr+n]
        curr += n
        test_cases.append((arr, k))
    
    if possible and len(test_cases) == T and curr == len(tokens):
        for arr, k in test_cases:
            print(get_max_diamonds(arr, k))
        return

    # Another possibility: arr then k for each test case
    # If none of the above, process line by line assuming pairs of (arr, k)
    idx = 0
    if len(lines) % 2 == 1:
        idx = 1 # skip T
    while idx < len(lines):
        arr = parse_ints(lines[idx])
        k = parse_ints(lines[idx+1])[0]
        print(get_max_diamonds(arr, k))
        idx += 2

def get_max_diamonds(arr, k):
    pq = [-x for x in arr]
    heapq.heapify(pq)
    ans = 0
    for _ in range(k):
        if not pq:
            break
        val = -heapq.heappop(pq)
        ans += val
        heapq.heappush(pq, -(val // 2))
    return ans

if __name__ == '__main__':
    solve()