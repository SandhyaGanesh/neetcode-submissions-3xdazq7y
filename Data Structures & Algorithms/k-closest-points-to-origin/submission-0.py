import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.sqrt(p[0]*p[0] + p[1]*p[1]),p) for p in points]
        heapq.heapify(distances)
        res = []
        for i in range(k):
            res.append(heapq.heappop(distances)[1])
        return res
