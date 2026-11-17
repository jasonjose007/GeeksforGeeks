# Sum Between k1'th and k2'th Smallest
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, Sorting, Heap

`current_arr` is empty, so skipped.
Line 2 -> `current_arr` set.
Line 3 -> `k1`, `k2` set -> prints result and resets.

Wait, what if `k1` and `k2` are given, and `k1` is 1-indexed?
Constraints: $1 \le k_1 < k_2 \le \text{arr.size()}$.
Let's verify indexing:
Sorted array: 0-indexed.
1st smallest: `sorted_arr[0]`
2nd smallest: `sorted_arr[1]`
...
$k_1$-th smallest: `sorted_arr[k1 - 1]`
$k_2$-th smallest: `sorted_arr[k2 - 1]`

Elements strictly between $k_1$-th smallest and $k_2$-th smallest are elements at 0-based indices from $(k_1 - 1) + 1 = k_1$ to $(k_2 - 1) - 1 = k_2 - 2$.
In Python slice notation `sorted_arr[start : end]`, `end` is exclusive, so `sorted_arr[k1 : k2 - 1]` includes indices $k_1, k_1+1, \dots, k_2-2$.
This correctly picks all elements strictly between $k_1$-th and $k_2$-th smallest!

Let'