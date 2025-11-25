def nearest_greater_closest(arr):
    n = len(arr)
    left, right = [-1]*n, [-1]*n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
    stack = []
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)
    res = []
    for i in range(n):
        l = left[i]
        r = right[i]
        if l == -1 and r == -1:
            res.append(-1)
        elif l == -1:
            res.append(arr[r])
        elif r == -1:
            res.append(arr[l])
        else:
            if i - l <= r - i:
                res.append(arr[l])
            else:
                res.append(arr[r])
    return res

n = int(input())
arr = list(map(int, input().split()))
print(*nearest_greater_closest(arr))
