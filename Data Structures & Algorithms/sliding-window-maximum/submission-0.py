import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windowElements = {}
        for i in range(k):
            windowElements[nums[i]] = windowElements.get(nums[i], 0) + 1
        startIdx = 0
        endIdx = k - 1

        h = []
        res = []
        for i in range(k):
            heapq.heappush(h, -nums[i])
        
        while startIdx <= endIdx < len(nums):
            print(h, windowElements)
            while -h[0] not in windowElements:
                heapq.heappop(h)
            res.append(-h[0])
            windowElements[nums[startIdx]] -= 1
            if windowElements[nums[startIdx]] == 0:
                del windowElements[nums[startIdx]]
            startIdx += 1
            endIdx += 1
            if endIdx < len(nums):
                windowElements[nums[endIdx]] = windowElements.get(nums[endIdx], 0) + 1
                heapq.heappush(h, -nums[endIdx])
        return res


        