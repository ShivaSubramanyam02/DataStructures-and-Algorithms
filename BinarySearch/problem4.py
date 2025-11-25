def lower_bound(arr, k):
    low, high = 0, len(arr) - 1
    ans = len(arr)   

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= k:
            ans = mid
            high = mid - 1   # move left to find first occurrence
        else:
            low = mid + 1    # move right

    return ans


n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(lower_bound(arr, k))
