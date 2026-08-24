class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def recurse(i, j):
            nonlocal s, t
            if (i,j) in memo:
                return memo[(i,j)]
            if j == len(t):
                return 1
            res = 0

            for r in range(i, len(s)):
                if t[j] == s[r]:
                    res += recurse(r+1, j+1)
            memo[(i,j)] = res
            return memo[(i,j)]
        
        return recurse(0,0)