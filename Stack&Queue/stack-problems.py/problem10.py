def validate_stack_sequences(pushed, popped):
    stack = []
    j = 0
    for x in pushed:
        stack.append(x)
        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return "YES" if not stack else "NO"

n = int(input())
pushed = list(map(int, input().split()))
popped = list(map(int, input().split()))
print(validate_stack_sequences(pushed, popped))
