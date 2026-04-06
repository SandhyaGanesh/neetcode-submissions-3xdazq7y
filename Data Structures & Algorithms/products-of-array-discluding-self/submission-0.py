class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1]*l
        prefixProduct = 1
        for i in range(0,l):
            res[i] *= prefixProduct
            prefixProduct *= nums[i]
        suffixProduct = 1
        for i in range(l-1,-1,-1):
            res[i] *= suffixProduct
            suffixProduct *= nums[i]
        return res

        