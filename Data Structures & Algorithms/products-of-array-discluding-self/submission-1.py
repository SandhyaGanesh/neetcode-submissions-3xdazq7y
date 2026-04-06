class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1]*l
        prefixProduct = 1
        suffixProduct = 1
        for i in range(0,l):
            res[i] *= prefixProduct
            prefixProduct *= nums[i]
            res[l-i-1] *= suffixProduct
            suffixProduct *= nums[l-i-1]
        return res

        