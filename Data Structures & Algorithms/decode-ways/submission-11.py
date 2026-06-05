class Solution:
    def twoDigitNumDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if int(s[0]) > 2 and s[1] == '0':
            return 0
        if 0 < int(s[0]) < 3 and s[1] == '0':
            return 1    
        if 0 < int(s[0]) <= 2 and int(s[1]) < 7:
            return 2
        else:
            return 1
        
    def numDecodings(self, s: str) -> int:
        l = len(s)
        if l == 1:
            return 1 if s != '0' else 0
        if l == 2:
            return self.twoDigitNumDecodings(s)

        dp = [0] * l
        dp[-1] = 1 if s[-1] != '0' else 0
        dp[-2] = self.twoDigitNumDecodings(s[l-2:])
        for i in range(l-3, -1, -1):
            if s[i] != '0' and dp[i+1]:
                dp[i] += dp[i+1]
            if self.twoDigitNumDecodings(s[i:i+2]) > 0 and int(s[i:i+2]) < 27 and dp[i+2]:
                dp[i] += dp[i+2]
        return dp[0]
