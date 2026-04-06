class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins = [0] + coins
        dp = [[0] * (amount + 1) for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0] = 1
        for i in range(1, amount + 1):
            dp[0][i] = 0
        for i in range(1, len(coins)):
            for j in range(1, amount + 1):
                include = dp[i][j - coins[i]] if j >= coins[i] else 0
                exclude = dp[i - 1][j]
                dp[i][j] = include + exclude
        return dp[-1][-1]