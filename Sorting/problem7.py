def etopower(x, n):
    def helper(n, x, term, fact, i):
        if i > n:
            return 0
        return term / fact + helper(n, x, term * x, fact * (i + 1), i + 1)
    
    return helper(n, x, 1.0, 1.0, 0)
