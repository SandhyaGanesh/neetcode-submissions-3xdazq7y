class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2 != 0:
            return False
        target = sum(nums)//2
        
        l = len(nums)
        
        dp = [['']*l for _ in range(target+1)]

        for i in range(l):
            dp[0][i] = True
        
        for i in range(1, target+1):
            dp[i][0] = True if nums[0] == i else False

        for i in range(1, target+1):
            for j in range(1, l):
                dp[i][j] = True if (nums[j] <= i and dp[i-nums[j]][j-1]) or dp[i][j-1] else False
        
        return dp[-1][-1]
        