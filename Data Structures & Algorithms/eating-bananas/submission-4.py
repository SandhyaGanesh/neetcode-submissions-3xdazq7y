import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = len(piles)
        piles.sort()

        i = 1
        e = max(piles)
        res = max(piles)

        while i < e:
            m = (i + e) // 2
            hoursNeeded = 0
            for b in piles:
                hoursNeeded += math.ceil(b/m)
            print(hoursNeeded)
            if hoursNeeded <= h:
                res = min(res, m)
                e = m
            elif hoursNeeded > h:
                i = m + 1
        
        return res