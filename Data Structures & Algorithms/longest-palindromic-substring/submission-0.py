class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        dp = [[False for _ in range(l)] for _ in range(l)]

        for i in range(l):
            dp[i][i] = True
        
        for i in range(0,l-1):
            dp[i][i+1] = True if s[i] == s[i+1] else False
        
        for j in range(2,l):
            r = 0
            c = j
            while c < l:
                dp[r][c] = True if (dp[r+1][c-1] and s[r] == s[c]) else False
                r += 1
                c += 1
        
        res = ""
        for i in range(l):
            for j in range(l):
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j+1]
        return res