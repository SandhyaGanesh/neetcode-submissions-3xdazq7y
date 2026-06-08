class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [1]*l
        for i in range(l-2, -1, -1):
            for index in range(i, l):
                dp[i] = max(dp[i], dp[index]+1) if nums[i] < nums[index] else dp[i]
        return max(dp)