#subset some



def subset_sum(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # Base case: sum = 0 is always possible (by picking nothing)
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the table
    for i in range(1, n + 1):
        for s in range(1, target + 1):
            if nums[i-1] <= s:
                # choice: include or exclude
                dp[i][s] = dp[i-1][s] or dp[i-1][s - nums[i-1]]
            else:
                # skip the number
                dp[i][s] = dp[i-1][s]

    return dp[n][target]
