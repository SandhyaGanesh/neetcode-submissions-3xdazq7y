class Solution:

    def getMostFreqChar(self, charMap):
        mx = 0
        cr = ''
        for i in range(ord('A'), ord('Z') + 1):
            c = chr(i)
            mx = max(charMap.get(c, 0), mx)
            if mx == charMap.get(c, 0):
                cr = c
        return cr

    def characterReplacement(self, s: str, k: int) -> int:
        l = len(s)
        if l <= 1:
            return l
        kcount = k
        charMap = {}

        sp = 0
        ep = 0
        charMap[s[sp]] = 1
        res = 0
        while sp <= ep < l - 1:
            ep += 1
            charMap[s[ep]] = charMap.get(s[ep], 0) + 1
            mfreq = self.getMostFreqChar(charMap)
            if charMap[mfreq] + k < ep - sp + 1:
                charMap[s[sp]] -= 1
                sp += 1
            res = max(res, ep - sp + 1)
        return res
