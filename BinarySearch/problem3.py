def upper_bound(arr, k):
    low, high = 0, len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > k:
            ans = mid
            high = mid - 1   

    return ans


n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(upper_bound(arr, k))