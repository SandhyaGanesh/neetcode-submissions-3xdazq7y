class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n < 0:
           x = 1/x
           n = -1 * n 
        for i in range(n):
            res = res*x
        return res