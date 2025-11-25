def first_missing_number(arr):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == mid:
            low = mid + 1
        else:
            high = mid - 1
    return low

User = int(input().strip())
for x in range(User):
    arr = list(map(int, input().split()))
    print(first_missing_number(arr))
