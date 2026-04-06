class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCounter = {}
        if len(s) != len(t):
            return False
        for c in s:
            charCounter[c] = charCounter.get(c, 0) + 1
        for c in t:
            if not charCounter.get(c) or charCounter[c] < 1:
                return False
            charCounter[c] -= 1
        return True
