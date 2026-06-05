class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        dp = [[False for i in range(l)] for i in range(l)]
        for i in range(l):
            dp[i][i] = True
        for i in range(l-1):
            dp[i][i+1] = True if s[i] == s[i+1] else False
        # for d in dp:
        #     print(d)

        loop = 0
        while loop < l - 2:
            for i in range(l - loop - 2):
                j = i + loop + 2
                # print(i, j)
                dp[i][j] = True if s[i] == s[j] and dp[i+1][j-1] else False
            loop += 1
        
        # for d in dp:
        #     print(d)
        start, end = 0, 0
        maxLen = 0
        for i in range(l):
            for j in range(i, l):
                if dp[i][j]:
                    maxLen += 1
        return maxLen