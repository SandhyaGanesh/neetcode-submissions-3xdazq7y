class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        dp = [[False]*l for _ in range(l)]

        for i in range(l):
            dp[i][i] = True
        for i in range(l-1):
            dp[i][i+1] = True if s[i] == s[i+1] else False
        
        for i in range(l-2):
            for r in range(l-2-i):
                c = 2 + i + r
                dp[r][c] = True if (s[r] == s[c] and dp[r+1][c-1]) else False
        
        # for r in dp:
        #     print(r)
        longestStr = ""
        longestLen = 0
        for i in range(l):
            for j in range(l):
                if dp[i][j] and j - i + 1 > longestLen:
                    longestLen = j - i + 1
                    longestStr = s[i:j+1]
        return longestStr