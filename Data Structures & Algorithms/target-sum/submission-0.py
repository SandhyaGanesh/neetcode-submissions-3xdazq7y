class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0

        def recurse(path):
            nonlocal res, target
            if len(path) == len(nums):
                res += 1 if sum(path) == target else 0
                return
            i = len(path)
            recurse(path + [nums[i]])
            recurse(path + [-nums[i]])
        
        recurse([])
        return res