class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        heap = []
        for num, freq in freqMap.items():
            heap.append((-1*freq, num))
        
        heapq.heapify(heap)
        result = []

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result