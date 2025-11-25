def super_digit(n, k):
    def helper(s):
        if len(s) == 1:
            return int(s)
        return helper(str(sum(int(d) for d in s)))
    
    
    initial_sum = sum(int(d) for d in n) * k
    return helper(str(initial_sum))


n, k = input().split()
k = int(k)
print(super_digit(n, k))
