class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        target = sum(nums)//2
        l = len(nums)
        nums = nums

        dp = [['x']*(l+1) for _ in range(target+1)]

        for i in range(l+1):
            dp[0][i] = True
        for i in range(1, target+1):
            dp[i][0] = False
        
        for i in range(1, target + 1):
            for j in range(1, l+1):
                if i == 3 and j == 2:
                    print(nums[j-1], dp[i - nums[j-1]][j-2])
                dp[i][j] = True if (nums[j-1] <= i and dp[i - nums[j-1]][j-1]) or dp[i][j-1] else False
        for d in dp:
            print(d)
        return dp[-1][-1]
