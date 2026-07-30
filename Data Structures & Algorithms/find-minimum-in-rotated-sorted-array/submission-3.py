class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        i = 0
        e = l

        while i < e:
            mid = (i+e) // 2
            if nums[i] < nums[mid] > nums[e-1]:
                i = mid + 1
            elif nums[i] > nums[mid] < nums[e-1]:
                e = mid + 1
            else:
                return min(nums[i], nums[mid], nums[e-1])

        return nums[mid]