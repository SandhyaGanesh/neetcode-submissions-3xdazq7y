class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = []
        for stone in stones:
            heapq.heappush(stoneHeap, -1 * stone)
        
        while len(stoneHeap) > 1:
            s1 = -1 * heapq.heappop(stoneHeap)
            s2 = -1 * heapq.heappop(stoneHeap)

            if s1 == s2:
                continue
            heapq.heappush(stoneHeap, -1*abs(s1-s2))
        
        return -1* stoneHeap[0] if stoneHeap else 0