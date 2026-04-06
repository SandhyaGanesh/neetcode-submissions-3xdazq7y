class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(index, curr):
            if index == len(nums):
                res.append(curr[:])
                return
            n = nums[index]
            curr.append(n)
            helper(index + 1, curr)
            curr.pop()
            helper(index + 1, curr)
        
        helper(0,[])
        return res