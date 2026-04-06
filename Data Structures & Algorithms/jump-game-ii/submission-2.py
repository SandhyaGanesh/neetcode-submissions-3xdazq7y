class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        jumpsSoFar = 0
        goal = l-1

        while goal > 0:
            i = 0
            while i < goal:
                if nums[i] + i >= goal:
                    goal = i
                    jumpsSoFar += 1
                    break
                i += 1
        
        return jumpsSoFar