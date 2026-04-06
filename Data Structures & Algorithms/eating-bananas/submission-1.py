import math

class Solution:
    def hoursNeeded(self, piles, speed):
        t = 0
        for pile in piles:
            t += math.ceil(pile/speed)
        return t

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) + 1
        t = sum(piles)
        res = r

        while l < r:
            mid = (l+r)//2
            hn = self.hoursNeeded(piles, mid)
            if hn == h:
                res = min(res,mid)
                r = mid
            elif hn < h:
                r = mid
            elif hn > h:
                l = mid + 1
        
        return r

        