def unbounded_knapsack(wt, val, W):
    n = len(wt)
    dp = [0] * (W + 1)
    for c in range(1, W + 1):
        for i in range(n):
            if wt[i] <= c:
                dp[c] = max(dp[c], dp[c - wt[i]] + val[i])
    return dp[W]
