class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        i = 0
        e = l - 1

        while i <= e:
            m = (i+e) // 2
            if nums[m] == target:
                return m
            elif nums[i] <= nums[m]:
                if target < nums[i] or target > nums[m]:
                    i = m + 1
                else:
                    e = m - 1
            else:
                if target > nums[e] or target < nums[m]:
                    e = m - 1
                else:
                    i = m + 1
        return -1