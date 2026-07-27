class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        nums.sort()
        result = []
        for i in range(l):
            target = -1 * nums[i]
            start = i + 1
            end = l - 1
            while start < end:
                currSum = nums[start] + nums[end]
                if currSum < target:
                    start += 1
                elif currSum > target:
                    end -= 1
                else:
                    result.append((nums[i], nums[start], nums[end]))
                    end -= 1
        return list(set(result))