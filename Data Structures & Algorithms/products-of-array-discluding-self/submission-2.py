class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefixSum = [1]*l
        suffixSum = [1]*l
        for i in range(l):
            if i > 0:
                prefixSum[i] = prefixSum[i-1] * nums[i-1]
            if i < l - 1:
                suffixSum[l-i-2] = suffixSum[l-i-1] * nums[l-i-1]
        res = [prefixSum[i]*suffixSum[i] for i in range(l)]
        return res
        