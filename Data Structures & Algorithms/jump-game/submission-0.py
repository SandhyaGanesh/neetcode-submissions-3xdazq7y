class Solution:
    def canJump(self, nums: List[int], i = 0) -> bool:
        if i == len(nums) - 1:
            return True
        for j in range(1, nums[i] + 1):
            if self.canJump(nums, i+j):
                return True
        return False