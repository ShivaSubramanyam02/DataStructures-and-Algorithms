def climbStairs(n):
    dp = [1, 1]  # base: 1 way for 0 steps and 1 step
    for i in range(2, n+1):
        new = dp[i-1] + dp[i-2]  # add previous two results
        dp.append(new)
    return dp[n]

print(climbStairs(5))  # 8
