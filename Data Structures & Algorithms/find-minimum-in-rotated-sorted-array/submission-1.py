class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        i = 0
        e = l
        res = nums[0]

        while i < e:
            m = (i+e) // 2
            print(i,m,e-1,nums[i], nums[m], nums[e-1])
            if nums[i] < nums[m]:
                res = min(res, nums[i])
                i = m + 1
            else:
                e = m
                res = min(res, nums[m])
        return res