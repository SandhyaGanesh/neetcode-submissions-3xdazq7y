class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        
        if l <= 1:
            return l
        
        startPtr = 0
        endPtr = 1
        res = 0
        charSet = set()
        charSet.add(s[0])

        while startPtr < endPtr < l:
            if s[endPtr] in charSet:
                while s[startPtr] != s[endPtr]:
                    charSet.remove(s[startPtr])
                    startPtr += 1
                charSet.remove(s[startPtr])
                startPtr += 1
            charSet.add(s[endPtr])
            endPtr += 1
            res = max(res, endPtr - startPtr)
        return res


        