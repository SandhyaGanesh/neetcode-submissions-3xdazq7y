class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        goal = l - 1
        hops = 0

        while goal - hops >= 0:
            if goal == 0:
                return True
            hops += 1
            if nums[goal-hops] >= hops:
                goal = goal-hops
                hops = 0
        
        return False
