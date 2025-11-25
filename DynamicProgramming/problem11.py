def rod_cutting(price, n):
    dp = [0] * (n + 1)
    for L in range(1, n + 1):
        for cut in range(1, L + 1):
            dp[L] = max(dp[L], price[cut - 1] + dp[L - cut])
    return dp[n]
