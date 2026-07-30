class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        i = 0
        e = l
        res = nums[i]

        while i < e:
            mid = (i+e) // 2
            res = min(res, nums[i], nums[e-1], nums[mid])
            if nums[mid] < nums[e-1]:
                e = mid + 1
            else:
                i = mid + 1

        return res