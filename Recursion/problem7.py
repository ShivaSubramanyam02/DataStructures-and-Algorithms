def power_sum(x, n, num=1):
    power = num ** n
    if x == 0:
        return 1
    if power > x:
        return 0

    
    include = power_sum(x - power, n, num + 1)
    exclude = power_sum(x, n, num + 1)
    return include + exclude


X, N = map(int, input().split())


print(power_sum(X, N))
