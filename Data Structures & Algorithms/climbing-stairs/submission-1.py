class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        lowerStep = 1
        higherStep = 2
        res = 0
        for i in range(3, n +1):
            res = lowerStep + higherStep
            lowerStep = higherStep
            higherStep = res
        return res