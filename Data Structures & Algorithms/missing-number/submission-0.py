class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        allNumXOR = 0
        for n in range(len(nums)+1):
            allNumXOR ^= n
        for n in nums:
            allNumXOR ^= n
        return allNumXOR