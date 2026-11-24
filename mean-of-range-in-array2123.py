# Mean of Range in Array
# Platform: GFG
# Difficulty: Easy
# Topics: Prefix Sum, Arrays

import sys

class Solution:
    def findMean(self, arr, queries):
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]
        
        ans = []
        for l, r in queries:
            total = prefix[r + 1] - prefix[l]
            count = r - l + 1
            ans.append(total // count)
        return ans

if __name__ == '__main__':
    input_data = sys.stdin.read().strip()
    if input_data:
        import ast
        lines = [line.strip() for line in input_data.splitlines() if line.strip()]
        
        # Check if input is formatted with brackets like [1, 2, 3]
        if lines[0].startswith('['):
            arr = ast.literal_eval(lines[0])
            queries = ast.literal_eval(lines[1])
            sol = Solution()
            res = sol.findMean(arr, queries)
            print(res)
        else:
            tokens = input_data.split()
            it = iter(tokens)
            try:
                # Could be: t test cases, or n q, arr, queries
                first = int(next(it))
                # Heuristic to detect format
                # If first token is t, or n
                # Check remaining tokens length
                remaining = len(tokens) - 1
                sol = Solution()
                
                # Check if standard (n, q, arr, queries) format
                # If remaining == first (which is n) + ...
                # Let's try to parse:
                second = int(next(it))
                n, q = first, second
                arr = [int(next(it)) for _ in range(n)]
                queries = [[int(next(it)), int(next(it))] for _ in range(q)]
                res = sol.findMean(arr, queries)
                print(*(res))
            except StopIteration:
                pass