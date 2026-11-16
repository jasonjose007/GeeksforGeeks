# Three Way Partitioning
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, Sorting

import sys

def threeWayPartition(arr, a, b):
    low = 0
    high = len(arr) - 1
    i = 0
    while i <= high:
        if arr[i] < a:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
            i += 1
        elif arr[i] > b:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1
        else:
            i += 1
    return arr

def is_valid_partition(arr, a, b):
    state = 0
    for x in arr:
        if x < a:
            if state > 0:
                return False
        elif a <= x <= b:
            if state > 1:
                return False
            state = max(state, 1)
        else:
            state = 2
    return True

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    try:
        tokens = [int(x) for x in input_data]
        num_tokens = len(tokens)
        
        if num_tokens >= 4:
            if tokens[0] + 3 == num_tokens:
                N = tokens[0]
                arr = tokens[1:1+N]
                a = tokens[1+N]
                b = tokens[1+N+1]
                threeWayPartition(arr, a, b)
                print("true" if is_valid_partition(arr, a, b) else "false")
                return
            
            T = tokens[0]
            curr = 1
            valid_T = True
            test_cases = []
            for _ in range(T):
                if curr >= num_tokens:
                    valid_T = False
                    break
                N = tokens[curr]
                if curr + 1 + N + 2 > num_tokens:
                    valid_T = False
                    break
                arr = tokens[curr+1 : curr+1+N]
                a = tokens[curr+1+N]
                b = tokens[curr+1+N+1]
                test_cases.append((arr, a, b))
                curr += 1 + N + 2
            
            if valid_T and curr == num_tokens:
                for arr, a, b in test_cases:
                    threeWayPartition(arr, a, b)
                    print("true" if is_valid_partition(arr, a, b) else "false")
                return

        a = tokens[-2]
        b = tokens[-1]
        arr = tokens[:-2]
        threeWayPartition(arr, a, b)
        print("true" if is_valid_partition(arr, a, b) else "false")

    except Exception:
        pass

if __name__ == '__main__':
    main()