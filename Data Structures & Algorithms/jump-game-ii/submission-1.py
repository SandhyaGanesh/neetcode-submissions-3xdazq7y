class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        jumpsSoFar = 0
        goal = l-1

        while goal > 0:
            for i in range(0, goal):
                if nums[i] + i >= goal:
                    goal = i
                    jumpsSoFar += 1
                    break
        
        return jumpsSoFar