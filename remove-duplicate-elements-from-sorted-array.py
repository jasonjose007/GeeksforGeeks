# Remove Duplicates Sorted Array
# Platform: GFG
# Difficulty: Easy
# Topics: two-pointer-algorithm, Arrays

def remove_duplicates(arr):
    if not arr:
        return []
    j = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    return arr[:j + 1]

if __name__ == "__main__":
    try:
        line = input().strip()
        while not line:
            line = input().strip()
        if line.startswith("["):
            line = line.strip("[]").replace(",", " ")
        arr = list(map(int, line.split()))
        res = remove_duplicates(arr)
        print(*res)
    except EOFError:
        pass