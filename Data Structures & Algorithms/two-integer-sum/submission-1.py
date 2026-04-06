class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for index, c in enumerate(nums):
            diff = target - c
            if diff in hashMap:
                return [hashMap[diff], index]
            hashMap[c] = index
        return []

        