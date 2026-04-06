class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap = {}
        for num in nums:
            if numMap.get(num, False):
                return True
            numMap[num] = True
        return False