class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        i = 0
        e = l

        while i < e <= l:
            middle = (i + e) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                e = middle
            elif nums[middle] < target:
                i = middle + 1
        return -1

        