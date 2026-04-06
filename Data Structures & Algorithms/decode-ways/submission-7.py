class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        if l < 2:
            return 1 if s[0] != '0' else 0
        
        dp = [0]*l
        dp[-1] = 1 if s[-1] != '0' else 0
        dp[-2] = 0 if s[-2] == '0' else (2 if (0 < int(s[-2:]) <= 26 and s[-1] != '0') else 1)

        for i in range(l-3, -1, -1):
            c = int(s[i:i+2])
            if s[i] == '0':
                dp[i] = 0
            else:
                if 0 < c <= 26:
                    dp[i] += dp[i+2]
                dp[i] += dp[i+1]
        
        return dp[0]