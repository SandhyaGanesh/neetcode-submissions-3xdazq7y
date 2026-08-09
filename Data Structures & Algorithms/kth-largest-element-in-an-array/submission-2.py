class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for _ in range(k):
            heapq.heappush(h, nums.pop())
        for num in nums:
            if num > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, num)
        return h[0]