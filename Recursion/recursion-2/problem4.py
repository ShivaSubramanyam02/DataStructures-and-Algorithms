def can_reach_one(n):
    while n > 1:
        if n % 10 == 0:
            n //= 10
        elif n % 20 == 0:
            n //= 20
        else:
            return False
    return n == 1

T = int(input())
for nick in range(T):
    N = int(input())
    if can_reach_one(N):
        print("Yes")
    else:
        print("No")
