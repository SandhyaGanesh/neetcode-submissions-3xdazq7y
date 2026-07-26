class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = {}

        for s in strs:
            tempList = [0]*26
            for c in s:
                tempList[ord(c)-ord('a')] += 1
            freqMap[tuple(tempList)] = freqMap.get(tuple(tempList), []) + [s]
        
        return list(freqMap.values())