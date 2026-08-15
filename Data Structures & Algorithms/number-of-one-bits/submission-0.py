class Solution:
    def hammingWeight(self, n: int) -> int:
        onesCount = 0
        while n:
            if n%2 == 1:
                onesCount += 1
                n -= 1
            n = n//2
        return onesCount
        