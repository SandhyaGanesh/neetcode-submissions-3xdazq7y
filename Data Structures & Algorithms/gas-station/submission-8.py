class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        if sum(cost) > sum(gas):
            return -1
        
        runningSum = 0
        minSum, minIndex = float("inf"), 0
        
        for i in range(l):
            runningSum += gas[i] - cost[i]
            if runningSum < minSum:
                minSum, minIndex = runningSum, i

        
        return (minIndex + 1)%l

        




