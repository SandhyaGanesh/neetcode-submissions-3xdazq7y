class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        startPtr = 0
        endPtr = l - 1
        while startPtr <= endPtr:
            if not s[startPtr].isalnum():
                startPtr += 1
                continue
            if not s[endPtr].isalnum():
                endPtr -= 1
                continue
            if s[startPtr].lower() != s[endPtr].lower():
                return False
            startPtr += 1
            endPtr -= 1
        
        return True