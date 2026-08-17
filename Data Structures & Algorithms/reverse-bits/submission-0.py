class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res += 2**(31-i) * (n&1)
            #print(n)
            n = n >> 1
            #print(n)
        return res