class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        goal = l-1
        
        for j in range(l-2, -1, -1):
            if nums[j] + j >= goal:
                goal = j

        return goal == 0