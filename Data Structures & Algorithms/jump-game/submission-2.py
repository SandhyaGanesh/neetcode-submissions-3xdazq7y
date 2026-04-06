class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        dp = [False]*l
        dp[l-1] = True
        
        for j in range(l-2, -1, -1):
            for i in range(1, nums[j]+1):
                dp[j] = True if i+j < l and dp[i+j] else dp[j]

        return dp[0]