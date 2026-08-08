import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for px, py in points:
            d = math.sqrt(px*px + py*py)
            heapq.heappush(h, (d, [px,py]))
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(h)[1])

        return result