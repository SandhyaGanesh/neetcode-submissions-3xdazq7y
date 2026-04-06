class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        res = 1001
        index = -1

        while l < r:
            mid = (l+r)//2
            if nums[l] <= nums[mid]:
                if res > nums[l]:
                    res = nums[l]
                    index = l
                l = mid + 1
            else:
                if res > nums[mid]:
                    res = nums[mid]
                    index = mid
                r = mid
        
        l = 0
        r = index
        while l < r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        l = index
        r = len(nums)
        while l < r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return -1