class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        gasSum = sum(gas)
        costSum = sum(cost)
        if costSum > gasSum:
            return -1
        
        diffList = [gas[i] - cost[i] for i in range(l)]
        runningSum = 0
        
        for i in range(l):
            diffList[i] += runningSum
            runningSum = diffList[i]
        
        return (diffList.index(min(diffList)) + 1)%l

        




