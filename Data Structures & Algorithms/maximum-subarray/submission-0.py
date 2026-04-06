class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        runningSum = nums[0]
        for i in range(1, len(nums)):
            if runningSum < 0:
                runningSum = nums[i]
            else:
                runningSum += nums[i]
            maxSum = max(maxSum, runningSum)   
        return maxSum        