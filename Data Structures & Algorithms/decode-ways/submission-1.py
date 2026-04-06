class Solution:
    def __init__(self):
        self.ret = 0
    
    def recurse(self, part, s):
        if len(part) == len(s):
            self.ret += 1
            return
        
        start = len(part)
        if start < len(s) and s[start] != '0':
            self.recurse(part+s[start], s)
        if start < start+1 < len(s) and self.isValid(s[start:start+2]):
            self.recurse(part+s[start:start+2], s)


    def isValid(self,s):
        return (10 <= int(s) <=26)

    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n < 1 or s[0] == '0':
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2 if (s[1] != '0' and self.isValid(s[:2])) else 1
        
        self.recurse('', s)
        return self.ret