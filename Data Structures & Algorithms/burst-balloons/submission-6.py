class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}

        def recurse(t):
            if t in memo:
                return memo[t]
            if len(t) == 1:
                return t[0]
            
            maxRes = 0
            i = 0
            for num in t:
                prevElement = 1 if i == 0 else t[i-1]
                currElement = t[i]
                nextElement = 1 if i == len(t)-1 else t[i+1]

                pop = prevElement*currElement*nextElement
                maxRes = max(maxRes, recurse(t[:i]+t[i+1:])+pop)

                i += 1
            memo[t] = maxRes
            return memo[t]
        
        return recurse(tuple(nums))