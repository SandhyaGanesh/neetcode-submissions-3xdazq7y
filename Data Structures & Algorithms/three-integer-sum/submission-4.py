class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        res = set()
        
        nums.sort()

        for i in range(l-2):
            ptr1 = i
            ptr2 = i + 1
            ptr3 = l - 1

            while ptr2 < ptr3:
                currSum = nums[ptr2] + nums[ptr3]
                target = nums[ptr1] * -1

                if currSum == target:
                    res.add(tuple([nums[ptr1], nums[ptr2], nums[ptr3]]))
                    ptr2 += 1
                    ptr3 -= 1
                elif currSum < target:
                    ptr2 += 1
                elif currSum > target:
                    ptr3 -= 1

        return list(res)


