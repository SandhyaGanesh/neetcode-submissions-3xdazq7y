class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0
        minCost = [0 for _ in range(len(cost) + 1)]
        minCost[0] = 0
        minCost[1] = 0
        for i in range(2, len(cost)+1):
            minCost[i] = min(minCost[i-1]+cost[i-1], minCost[i-2]+cost[i-2])
        return minCost[-1]

            