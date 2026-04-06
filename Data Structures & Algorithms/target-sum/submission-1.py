class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0

        def recurse(pathSum, i):
            nonlocal res, target
            if i == len(nums):
                res += 1 if pathSum == target else 0
                return

            recurse(pathSum + nums[i], i+1)
            recurse(pathSum - nums[i], i+1)
        
        recurse(0, 0)
        return res