class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robHelper(nums: List[int]) -> int:
            l = len(nums)
            if l == 1:
                return nums[0]
            dp = [0]*l
            dp[0] = nums[0]

            for i in range(1, l):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])

            return dp[-1]
        return max(robHelper(nums[1:]), robHelper(nums[:-1]))