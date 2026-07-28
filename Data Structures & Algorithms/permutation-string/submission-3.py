class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        if l2 < l1:
            return False
        
        s1Freq = [0]*26
        for c in s1:
            s1Freq[ord(c)-ord('a')] += 1
        s1Freq = tuple(s1Freq)

        s2Freq = [0]*26
        for i in range(l1):
            s2Freq[ord(s2[i])-ord('a')] += 1

        i = 0
        e = l1 - 1

        while e < l2:
            if tuple(s2Freq) == s1Freq:
                return True
            s2Freq[ord(s2[i])-ord('a')] -= 1
            i += 1
            e += 1
            if e < l2:
                s2Freq[ord(s2[e])-ord('a')] += 1
        
        return False