class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqDict = {}
        for c in s:
            freqDict[c] = freqDict.get(c, 0) + 1
        for c in t:
            if not freqDict.get(c, 0):
                return False
            freqDict[c] = freqDict[c] - 1
        for num, freq in freqDict.items():
            if freq != 0:
                return False
        return True