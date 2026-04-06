class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqDict = defaultdict(bool)
        for num in nums:
            if num in freqDict:
                return True
            freqDict[num] = True
        return False