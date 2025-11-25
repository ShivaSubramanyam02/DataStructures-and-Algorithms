def count_subsets(nums, target):
    n = len(nums)
    dp = [[0] * (target + 1) for _ in range(n + 1)]

    # Base case: one subset (empty set) makes sum = 0
    for i in range(n + 1):
        dp[i][0] = 1

    # Fill table
    for i in range(1, n + 1):
        for s in range(0, target + 1):
            if nums[i-1] <= s:
                # include + exclude
                dp[i][s] = dp[i-1][s] + dp[i-1][s - nums[i-1]]
            else:
                # skip the element
                dp[i][s] = dp[i-1][s]

    return dp[n][target] 
