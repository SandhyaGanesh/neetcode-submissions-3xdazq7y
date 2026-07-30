import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        e = max(piles)
        result = e

        while i <= e:
            mid = (i+e) // 2
            midHours = sum([math.ceil(p/mid) for p in piles])
            print(i, e, mid, midHours)
            if midHours <= h:
                e = mid - 1
                result = mid
            else:
                i = mid + 1
        return result
            
