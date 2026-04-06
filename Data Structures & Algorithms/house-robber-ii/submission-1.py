class Solution:
    def robLinearHouses(self, nums: List[int]):
        if not nums:
            return 0
        
        l = len(nums)
        if l <= 2:
            return max(nums)
        dp = [0]*l
        dp[0] = nums[0]
        dp[1] = nums[1]
        
        for i in range(1, l):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        l = len(nums)
        if l <= 2:
            return max(nums)
        return max(self.robLinearHouses(nums[:-1]), self.robLinearHouses(nums[1:]))