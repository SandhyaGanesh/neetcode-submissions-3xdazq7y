class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l <= 1:
            return l

        indMap = {}

        startIdx = 0
        endIdx = 0
        indMap[s[startIdx]] = 0
        res = 0

        while startIdx <= endIdx < l - 1:
            endIdx += 1
            if s[endIdx] in indMap:
                newStartIdx = indMap[s[endIdx]] + 1
                for i in range(startIdx, newStartIdx):
                    #print(indMap)
                    del indMap[s[i]]
                startIdx = newStartIdx
            indMap[s[endIdx]] = endIdx
            res = max(res, endIdx - startIdx + 1)
        
        return res

        