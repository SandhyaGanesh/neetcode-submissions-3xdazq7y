class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        dp = [[1,1] for n in nums]
        dp[0] = [nums[0], nums[0]]
        for i in range(1, l):
            if nums[i] > 0:
                dp[i][0] = max(dp[i-1][0]*nums[i], nums[i])
                dp[i][1] = min(dp[i-1][1]*nums[i], nums[i])
            elif nums[i] < 0:
                dp[i][0] = max(dp[i-1][1]*nums[i], nums[i])
                dp[i][1] = min(dp[i-1][0]*nums[i], nums[i])
        
        res = nums[0]
        for ma, mi in dp:
            res = max(ma, res)
        if 0 in nums and 1 not in nums and res == 1:
            return 0
        return res