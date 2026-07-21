class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []
        def recurse(i):
            nonlocal target
            if sum(combination) == target:
                result.append(combination.copy())
                return
            if sum(combination) > target or i == len(nums):
                return
            combination.append(nums[i])
            recurse(i)
            combination.pop()
            recurse(i+1)
        recurse(0)
        return result
