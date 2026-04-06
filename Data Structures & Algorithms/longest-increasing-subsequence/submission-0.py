class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        
        def dfs(i, path):
            if i == len(nums):
                print(path)
                res.append(len(path))
                return
            n = nums[i]
            prevNum = path[-1] if path else -1*float("inf")
            if n > prevNum:
                path.append(n)
                dfs(i+1, path)
                path.pop()
            dfs(i+1, path)
        
        dfs(0, [])
        print(res)
        return max(res)