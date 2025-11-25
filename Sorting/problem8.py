def super_digit(n, k):
    def helper(s):
        if len(s) == 1:
            return int(s)
        digit_sum = sum(int(d) for d in s)
        return helper(str(digit_sum))
    
    initial_sum = sum(int(d) for d in n) * k
    return helper(str(initial_sum))
