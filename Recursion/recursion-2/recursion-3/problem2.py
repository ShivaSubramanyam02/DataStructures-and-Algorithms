def A(n):
    if n == 0 or n == 1:
        return 10
    elif n == 2:
        return -19
    elif n > 2:
        if n % 6 == 0:
            return (n // 6) + (A(n-1) + A(n-3))
        elif n % 2 == 0 and n % 3 != 0:
            return (n // 2) - (A(n-1) + A(n-2))
        elif n % 3 == 0 and n % 2 != 0:
            return (n // 3) + (A(n-1) + A(n-3))
        else:
            return A(n-1)


n = int(input())
print(A(n))
