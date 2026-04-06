class Solution:
    def compareMaps(self, tMap, sMap):
        for i, freq in enumerate(tMap):
            if sMap[i] < freq:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        tMap = [0]*60
        sMap = [0]*60

        for c in t:
            tMap[ord(c) - ord('A')] += 1
        
        if len(s) < len(t) or len(s) == 0 or len(t) == 0:
            return ""

        start = 0
        end = 0
        res = ""
        lres = len(s) + 1

        while end < len(s):
            sMap[ord(s[end]) - ord('A')] += 1
            end += 1
            while self.compareMaps(tMap, sMap):
                if lres > end - start:
                    res = s[start:end]
                    lres = end - start
                sMap[ord(s[start]) - ord('A')] -= 1
                start += 1
        
        return res if lres != len(s) + 1 else ""
                



        
