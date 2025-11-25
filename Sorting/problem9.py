def find_term(n):
    if n == 0 or n == 1:
        return 10
    if n == 2:
        return -19

    if n % 2 == 0 and n % 3 == 0:
        return (n // 6) + find_term(n - 1) + find_term(n - 3)
    elif n % 2 == 0:
        return (n // 2) - (find_term(n - 1) + find_term(n - 2))
    elif n % 3 == 0:
        return (n // 3) + find_term(n - 1) + find_term(n - 3)
    else:
        return find_term(n - 1)
