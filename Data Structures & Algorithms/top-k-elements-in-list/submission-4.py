class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        freqList = []
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        for num, freq in freqMap.items():
            freqList.append((freq, num))
        freqList.sort(reverse=True)
        return [item[1] for item in freqList[:k]]