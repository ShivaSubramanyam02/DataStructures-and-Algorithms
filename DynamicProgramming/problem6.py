#equal sum partition problem


def can_partition(nums):
    total = sum(nums)

    # If total is odd, cannot partition equally
    if total % 2 != 0:
        return False

    target = total // 2
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # Base case: sum 0 is always possible
    for i in range(n + 1):
        dp[i][0] = True

    # Fill DP table
    for i in range(1, n + 1):
        for s in range(1, target + 1):
            if nums[i-1] <= s:
                dp[i][s] = dp[i-1][s] or dp[i-1][s - nums[i-1]]
            else:
                dp[i][s] = dp[i-1][s]

    return dp[n][target]
