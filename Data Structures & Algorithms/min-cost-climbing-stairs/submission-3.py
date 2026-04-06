class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0
        minCost = [0 for _ in range(len(cost) + 1)]
        minCost0 = 0
        minCost1 = 0
        for i in range(2, len(cost)+1):
            t = minCost1
            minCost1 = min(minCost1+cost[i-1], minCost0+cost[i-2])
            minCost0 = t

        return minCost1

            