class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dp = [0]*(len(cost))
        dp[0] = 0
        dp[1] = 0
        for step in range(2, len(cost)):
            dp[step] = min(dp[step-1]+cost[step-1], dp[step-2]+cost[step-2])
        return dp[-1]