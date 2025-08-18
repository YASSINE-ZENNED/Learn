class Solution(object):
    def new21Game(self, n, k, maxPts):
        if k == 0:
            return 1.0 if n >= 0 else 0.0
        if n >= k + maxPts - 1:
            return 1.0

        dp = defaultdict(float)
        dp[0] = 1.0
        window_sum = 1.0

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts

            if i < k:
                window_sum += dp[i]
            if i >= maxPts:
                window_sum -= dp[i - maxPts]

        return sum(dp[i] for i in range(k, n + 1))

"""
If you calculate the same thing multiple times, store it instead.
Use a "sliding window" to maintain running totals. Don't recalculate - reuse!
"""