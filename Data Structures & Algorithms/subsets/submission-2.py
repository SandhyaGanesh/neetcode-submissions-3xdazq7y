class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsetList = []
        l = len(nums)
        def recurse(i, l, running):
            if i == l:
                subsetList.append(running)
                return
            recurse(i+1, l, running + [nums[i]])
            recurse(i+1, l, running)
        recurse(0, l, [])
        return subsetList
            