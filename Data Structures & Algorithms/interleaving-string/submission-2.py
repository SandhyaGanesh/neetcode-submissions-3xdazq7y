class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        dp[-1][-1] = True
        for i in range(len(s1)-1, -1, -1):
            dp[i][-1] = True if s1[i] == s3[i+len(s2)] and dp[i+1][-1] else False
        for j in range(len(s2)-1, -1, -1):
            dp[-1][j] = True if s2[j] == s3[j+len(s1)] and dp[-1][j+1] else False
        
        for i in range(len(s1)-1, -1, -1):
            for j in range(len(s2)-1, -1, -1):
                dp[i][j] = True if ((s1[i] == s3[i+j] and dp[i+1][j]) or (s2[j] == s3[i+j] and dp[i][j+1])) else False
        
        return dp[0][0]