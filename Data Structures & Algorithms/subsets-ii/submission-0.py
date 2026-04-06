class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def helper(index, curr):
            if index == len(nums):
                res.append(curr[:])
                return
            
            n = nums[index]
            curr.append(n)
            helper(index + 1, curr)
            curr.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            helper(index + 1, curr)
            
        helper(0, [])
        return res