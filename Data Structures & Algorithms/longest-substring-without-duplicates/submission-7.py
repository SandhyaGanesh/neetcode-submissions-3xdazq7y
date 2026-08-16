class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        freqMap = [0]*128
        maxLen = 0

        start = 0
        for i in range(l):
            #print(s[start], s[i])
            if freqMap[ord(s[i])] == 0:
                maxLen = max(maxLen, i - start + 1)
                freqMap[ord(s[i])] += 1
            else:
                while s[start] != s[i]:
                    freqMap[ord(s[start])] -= 1
                    start += 1
                start += 1
        return maxLen


        

