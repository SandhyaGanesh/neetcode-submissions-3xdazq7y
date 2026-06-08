class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [False]*(l+1)
        dp[l] = True
        for i in range(l-1, -1, -1):
            for word in wordDict:
                if i+len(word) <= l and s[i:i+len(word)] == word and dp[i+len(word)]:
                    dp[i] = True
                    break
        return dp[0]