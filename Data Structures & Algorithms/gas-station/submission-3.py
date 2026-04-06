class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        arr = [gas[i]-cost[i] for i in range(l)]
        if sum(arr) < 0:
            return -1
        
        r = 0
        path = 0
        for i in range(len(arr)):
            path += arr[i]
            if path < 0:
                r = i + 1
                path = 0
        return r

