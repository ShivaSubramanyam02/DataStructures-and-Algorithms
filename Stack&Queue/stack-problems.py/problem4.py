def nearest_smaller_left(arr):
    stack, res = [], []
    for a in arr:
        while stack and stack[-1] >= a:
            stack.pop()
        res.append(stack[-1] if stack else -1)
        stack.append(a)
    return res

n = int(input())
arr = list(map(int, input().split()))
print(nearest_smaller_left(arr))
