class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        freqBucket = [[] for i in range(len(nums) + 1)]
        for num, freq in freqMap.items():
            freqBucket[freq].append(num)
        
        freqSortedArr = []
        for freqNum in freqBucket:
            freqSortedArr.extend(freqNum)
        
        res = []
        for i in range(k):
            res.append(freqSortedArr.pop())
        
        return res

        