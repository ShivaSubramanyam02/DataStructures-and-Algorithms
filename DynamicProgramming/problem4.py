def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for x in range(n + 1)]

    for i in range(1, n + 1):          # items
        for w in range(1, W + 1):      # capacities
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w],values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

    





weights = [1, 2, 3]
values = [6, 10, 12]
W = 5
print(knapsack(weights, values, W))
