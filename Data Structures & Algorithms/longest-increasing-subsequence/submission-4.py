class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxLen = 1
        indexMap = {}
        
        def dfs(index, l):
            if index in indexMap:
                if indexMap[index] >= l:
                    return
            indexMap[index] = l
            nonlocal maxLen 
            maxLen = max(maxLen, l)
            for i in range(index+1, len(nums)):
                if nums[i] > nums[index]:
                    dfs(i, l+1)
                else:
                    dfs(i, 1)
        dfs(0, 1)
        return maxLen