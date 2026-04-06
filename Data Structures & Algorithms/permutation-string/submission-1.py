class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1FreqMap = [0 for i in range(26)]
        slidingFreqMap = [0 for i in range(26)]

        for c in s1:
            s1FreqMap[ord(c) - ord('a')] += 1
        
        if len(s1) > len(s2):
            return False
        
        for i in range(len(s1)):
            slidingFreqMap[ord(s2[i]) - ord('a')] += 1
        
        if s1FreqMap == slidingFreqMap:
            return True
        
        s = 0
        e = len(s1)
        while e < len(s2):
            print(s1FreqMap, slidingFreqMap)
            if s1FreqMap == slidingFreqMap:
                return True
            slidingFreqMap[ord(s2[s]) - ord('a')] -= 1
            s += 1
            slidingFreqMap[ord(s2[e]) - ord('a')] += 1
            e += 1
        
        if s1FreqMap == slidingFreqMap:
            return True
        return False
