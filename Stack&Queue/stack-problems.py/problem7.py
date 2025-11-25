def nearest_greater_right(arr):
    stack, res = [], [0]*len(arr)
    for i in range(len(arr)-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(arr[i])
    return res

n = int(input())
arr = list(map(int, input().split()))
print(*nearest_greater_right(arr))
