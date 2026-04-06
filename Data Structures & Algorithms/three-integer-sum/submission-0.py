class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        fixIndex = 0
        res = set()
        while fixIndex < l - 2:
            s = fixIndex + 1
            e = l - 1
            target = 0 - nums[fixIndex]
            while s < e:
                if nums[s] + nums[e] > target:
                    e -= 1
                elif nums[s] + nums[e] < target:
                    s += 1
                else:
                    res.add((nums[fixIndex], nums[s], nums[e]))
                    s += 1
                    e -= 1
            fixIndex += 1
        resList = []
        for r in res:
            resList.append(list(r))
        return (resList)