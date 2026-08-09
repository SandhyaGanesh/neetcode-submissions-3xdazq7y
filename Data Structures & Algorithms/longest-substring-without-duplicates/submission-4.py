class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l == 1:
            return 1
        
        windowSet = set()
        i = 0
        e = 0
        result = 0

        while i <= e < l:
            if s[e] in windowSet:
                while s[i] != s[e]:
                    windowSet.remove(s[i])
                    i += 1
                windowSet.remove(s[i])
                i += 1
            windowSet.add(s[e])
            e += 1
            result = max(result, e - i)
        
        return result


        

