class Solution:
    def maxCoins(self, nums):
        l = len(nums)
        nums = [1] + nums + [1]

        dp = [[0 for _ in range(l + 2)] for _ in range(l + 2)]
        for left in range(l, 0, -1):
            for right in range(left, l + 1):
                for i in range(left, right + 1):
                    coins = nums[left - 1] * nums[i] * nums[right + 1]
                    coins += dp[left][i - 1] + dp[i + 1][right]
                    dp[left][right] = max(dp[left][right], coins)

        return dp[1][l]