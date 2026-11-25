# Possible Words From Phone Digits
# Platform: GFG
# Difficulty: Medium
# Topics: Arrays, Strings, Mathematics, Recursion, Backtracking

import sys
import itertools
import re

class Solution:
    def possibleWords(self, arr):
        mapping = {
            2: "abc", 3: "def", 4: "ghi",
            5: "jkl", 6: "mno", 7: "pqrs",
            8: "tuv", 9: "wxyz"
        }
        
        pools = [mapping[d] for d in arr if d in mapping and mapping[d]]
        if not pools:
            return []
            
        return [''.join(p) for p in itertools.product(*pools)]

def main():
    input_text = sys.stdin.read().strip()
    if not input_text:
        return
    
    sol = Solution()
    
    # Parse integers from input
    tokens = re.findall(r'\d+', input_text)
    if not tokens:
        return
        
    nums = [int(x) for x in tokens]
    
    # Check if first token is length N of array
    if len(nums) > 1 and nums[0] == len(nums) - 1:
        arr = nums[1:]
    else:
        arr = nums
        
    ans = sol.possibleWords(arr)
    print(" ".join(ans))

if __name__ == '__main__':
    main()