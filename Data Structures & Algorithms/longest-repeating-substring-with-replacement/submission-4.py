class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = len(s)

        if l <= 1:
            return l
        
        charMap = [0] * 26
        startPtr = 0
        endPtr = 0
        res = 1

        while startPtr <= endPtr <= l:
            winLen = endPtr - startPtr
            print(startPtr, endPtr, winLen, charMap)
            if winLen - max(charMap) <= k:
                res = max(res, winLen)
                if endPtr < l:
                    charMap[ord(s[endPtr]) - ord('A')] += 1
                endPtr += 1
            else:
                charMap[ord(s[startPtr]) - ord('A')] -= 1
                startPtr += 1
        return res
        