class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(index, curr):
            if sum(curr) == target:
                res.append(curr[:])
                return
            if sum(curr) > target or index == len(nums):
                return
            n = nums[index]
            curr.append(n)
            helper(index, curr)
            curr.pop()
            helper(index + 1, curr)
        
        helper(0,[])
        return res