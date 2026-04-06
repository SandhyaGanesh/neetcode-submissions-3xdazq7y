class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMap = [0]*26
        for c in s:
            freqMap[ord(c)-ord('a')] += 1
        for c in t:
            freqMap[ord(c)-ord('a')] -= 1    
        
        for c in range(26):
            if freqMap[c] != 0:
                return False

        return True
