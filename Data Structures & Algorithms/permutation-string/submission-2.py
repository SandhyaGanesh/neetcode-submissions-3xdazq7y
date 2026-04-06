class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1l = len(s1)
        s2l = len(s2)

        if s2l < s1l:
            return False
        
        charDict = {}
        for c in s1:
            charDict[c] = charDict.get(c, 0) + 1

        startPtr = 0
        endPtr = s1l - 1

        currDict = {}
        for i in range(startPtr, endPtr + 1):
            currDict[s2[i]] = currDict.get(s2[i], 0) + 1
        
        while endPtr < s2l:
            print(currDict, charDict)
            if currDict == charDict:
                return True
            currDict[s2[startPtr]] -= 1
            if currDict[s2[startPtr]] == 0:
                del currDict[s2[startPtr]]
            startPtr += 1
            endPtr += 1
            if endPtr < s2l:
                currDict[s2[endPtr]] = currDict.get(s2[endPtr], 0) + 1
        
        return False
        
        