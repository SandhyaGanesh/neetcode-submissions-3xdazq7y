class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        seqLenMap = {}
        for num in nums:
            if num - 1 in numSet:
                continue
            seqLenMap[num] = 1
        print(seqLenMap)
        for startNum in seqLenMap.keys():
            end = startNum + 1
            while end in numSet:
                seqLenMap[startNum] += 1
                end += 1
        res = 0
        for l in seqLenMap.values():
            res = max(res,l)
        return res