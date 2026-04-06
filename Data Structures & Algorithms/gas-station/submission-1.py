class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        arr = [gas[i]-cost[i] for i in range(l)]
        if sum(arr) < 0:
            return -1
        
        r = 0
        for res in range(l):
            path = [i for i in range(res, len(gas))] + [i for i in range(0, res)]
            curr = 0
            flag = False
            for i in path:
                curr += gas[i] - cost[i]
                if curr < 0:
                    flag = True
                    break
            if not flag:
                r = res
        return r

