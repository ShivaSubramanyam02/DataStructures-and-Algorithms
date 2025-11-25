def count_subsets(arr, n, x):
    if x == 0:
        return 1
    if n == 0:
        return 0
    if arr[n - 1] <= x:
        return count_subsets(arr, n - 1, x - arr[n - 1]) + count_subsets(arr, n - 1, x)
    else:
        return count_subsets(arr, n - 1, x)


n = int(input())
arr = list(map(int, input().split()))
x = int(input())
print(count_subsets(arr, n, x))
