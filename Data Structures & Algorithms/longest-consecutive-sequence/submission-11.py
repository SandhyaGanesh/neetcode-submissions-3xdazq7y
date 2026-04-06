class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        if len(s) == 1:
            return 1
        res = 1
        for num in nums:
            if num - 1 in s:
                continue
            l = 0
            i = num +1
            while i in s:
                l += 1
                i += 1
            res = max(l, res)
        return res + 1
        