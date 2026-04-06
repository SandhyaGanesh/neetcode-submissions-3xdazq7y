class Solution:
    def isSubsetSum(self, nums, target) -> bool:
        print(nums, target)
        if len(nums) == 1:
            return True if sum(nums) == target else False
        for i in range(len(nums)):
            target -= nums[i]
            if target == 0:
                return True
            elif target > 0:
                if self.isSubsetSum(nums[:i]+nums[i+1:], target):
                    return True
            target += nums[i]
        return False

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        return self.isSubsetSum(nums, sum(nums)//2)