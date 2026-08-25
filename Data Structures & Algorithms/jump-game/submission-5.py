class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        dp = [False for _ in range(l)]
        dp[l-1] = True

        for i in range(l-2, -1, -1):
            for j in range(nums[i]+1):
                if i+j < l and dp[i+j]:
                    dp[i] = True
        return dp[0]