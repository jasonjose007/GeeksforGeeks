# Range Vowel Count Queries
# Platform: GFG
# Difficulty: Medium
# Topics: Prefix Sum, Strings

import sys
import re

def main():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    
    s_match = re.search(r's\s*=\s*["\']([^"\']+)["\']', input_data)
    if s_match:
        s = s_match.group(1)
        rest_of_text = input_data[s_match.end():]
    else:
        lines = [line.strip() for line in input_data.splitlines() if line.strip()]
        s = re.sub(r'^s\s*=\s*', '', lines[0]).strip('"\'')
        rest_of_text = '\n'.join(lines[1:])
    
    vowels = set("aeiouAEIOU")
    n = len(s)
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + (1 if s[i] in vowels else 0)
        
    nums = list(map(int, re.findall(r'\d+', rest_of_text)))
    
    if len(nums) % 2 != 0 and nums[0] == (len(nums) - 1) // 2:
        query_nums = nums[1:]
    else:
        query_nums = nums
        
    ans = []
    for i in range(0, len(query_nums), 2):
        l, r = query_nums[i], query_nums[i+1]
        ans.append(pref[r + 1] - pref[l])
        
    print(ans)

if __name__ == '__main__':
    main()