def countWays(x, n, num=1):
    if x == 0:
        return 1
    if x < 0 or num ** n > x:
        return 0
    return countWays(x - num ** n, n, num + 1) + countWays(x, n, num + 1)
x = 10
n = 2
print(countWays(x, n))  
