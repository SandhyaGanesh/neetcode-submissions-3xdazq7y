class Solution:
    def __init__(self):
        self.memo = {}
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        strLen = len(s)
        dictLen = len(wordDict)
        dp = [False]*strLen

        for i in range(strLen - 1, -1, -1):
            for word in wordDict:
                print(s[i:], i, word, len(word), strLen)
                if s[i:].startswith(word) and not dp[i]:
                    if i + len(word) < strLen:
                        dp[i] = dp[i + len(word)]
                    else:
                        dp[i] = True
        print(dp)
        return dp[0]