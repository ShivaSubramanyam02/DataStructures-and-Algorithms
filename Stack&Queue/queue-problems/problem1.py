def is_valid_stack_sequence(pushed, popped):
    stack = []
    j = 0
    for val in pushed:
        stack.append(val)
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return j == len(popped)

T = int(input())
for _ in range(T):
    n = int(input())
    pushed = list(map(int, input().split()))
    popped = list(map(int, input().split()))
    print("YES" if is_valid_stack_sequence(pushed, popped) else "NO")
