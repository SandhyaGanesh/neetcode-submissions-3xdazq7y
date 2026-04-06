class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*len(t) for _ in range(len(s))]

        dp[0][0] = 0 if t[0] != s[0] else 1
        for i in range(1, len(s)):
            if t[0] == s[i]:
                dp[i][0] = dp[i-1][0] + 1
            else:
                dp[i][0] = dp[i-1][0]
        
        for j in range(1, len(t)):
            dp[0][j] = 0
        
        for i in range(1, len(s)):
            for j in range(1, len(t)):
                if s[i] == t[j]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]