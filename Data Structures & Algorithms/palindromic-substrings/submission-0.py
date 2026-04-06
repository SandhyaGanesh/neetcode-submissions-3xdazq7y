class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        dp = [[False for _ in range(l)] for _ in range(l)]

        for i in range(l):
            dp[i][i] = True
        
        for i in range(l-1):
            dp[i][i+1] = True if s[i] == s[i+1] else False
        
        for j in range(2, l):
            r = 0
            c = j
            while c < l:
                dp[r][c] = True if (s[r] == s[c] and dp[r+1][c-1]) else False
                r += 1
                c += 1
        
        res = 0
        for i in range(l):
            for j in range(l):
                if dp[i][j]:
                    res += 1
        
        return res