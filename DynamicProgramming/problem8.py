def min_subset_sum_diff(nums):
    n = len(nums)
    total_sum = sum(nums)
    target = total_sum // 2

    # DP table for subset sum (True/False)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # Base case: sum = 0 is always possible
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the DP table
    for i in range(1, n + 1):
        for s in range(1, target + 1):
            if nums[i-1] <= s:
                dp[i][s] = dp[i-1][s] or dp[i-1][s - nums[i-1]]
            else:
                dp[i][s] = dp[i-1][s]

    # Find the largest 's' that is True (possible subset sum)
    for s in range(target, -1, -1):
        if dp[n][s]:
            s1 = s
            break

    # Minimum difference
    return total_sum - 2 * s1  
