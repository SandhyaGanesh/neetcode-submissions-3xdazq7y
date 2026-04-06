class Solution:
    def __init__(self):
        self.memo = {}
    def canJump(self, nums: List[int], i = 0) -> bool:
        if i in self.memo:
            return self.memo[i]
        if i == len(nums) - 1:
            self.memo[i] = True
            return True
        for j in range(1, nums[i] + 1):
            if self.canJump(nums, i+j):
                self.memo[i] = True
                return True
        self.memo[i] = False
        return False