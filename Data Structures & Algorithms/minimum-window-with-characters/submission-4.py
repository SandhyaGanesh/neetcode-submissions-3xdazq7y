class Solution:
    def isSubset(self, sMap, tMap):
        for key, value in tMap.items():
            if key not in sMap or sMap[key] < tMap[key]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        lt = len(t)
        ls = len(s)

        if ls < lt:
            return ""
        
        tMap = {}
        sMap = {}

        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
        
        sIdx = 0
        eIdx = 0

        while eIdx < ls:
            print(eIdx)
            if s[eIdx] in tMap:
                sMap[s[eIdx]] = sMap.get(s[eIdx], 0) + 1
            if self.isSubset(sMap, tMap):
                break
            eIdx += 1
        
        if not self.isSubset(sMap, tMap):
            return ""
        print(sIdx, eIdx)
        res = s[sIdx:eIdx+1]

        while sIdx <= eIdx < ls:
            if s[sIdx] not in tMap:
                sIdx += 1
                print("s[sIdx:eIdx+1], res", s[sIdx:eIdx+1], res)
                res = s[sIdx:eIdx+1] if len(s[sIdx:eIdx+1]) < len(res) else res
                print("res", res)
                continue
            tempMap = sMap.copy()
            print(tempMap)
            tempMap[s[sIdx]] -= 1
            if self.isSubset(tempMap, tMap):
                sMap[s[sIdx]] -= 1
                sIdx += 1
                print("2 s[sIdx:eIdx+1], res", s[sIdx:eIdx+1], res)
                res = s[sIdx:eIdx+1] if len(s[sIdx:eIdx+1]) < len(res) else res
                continue
            else:
                eIdx += 1
                if eIdx < ls and s[eIdx] in tMap:
                    sMap[s[eIdx]] = sMap.get(s[eIdx], 0) + 1
        
        return res

