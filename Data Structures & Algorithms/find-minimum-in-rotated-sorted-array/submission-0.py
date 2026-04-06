class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        res = 1001

        while l < r:
            mid = (l+r)//2
            if nums[l] <= nums[mid]:
                res = min(res, nums[l])
                l = mid + 1
                continue
            else:
                res = min(res, nums[mid])
                r = mid
        return res