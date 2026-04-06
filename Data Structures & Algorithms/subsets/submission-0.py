class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(nums, curr):
            if not nums:
                res.append(curr)
                return
            n = nums.pop()
            curr1 = curr
            curr2 = curr + [n]
            helper(nums.copy(), curr1)
            helper(nums.copy(), curr2)
        
        helper(nums.copy(), [])
        return res