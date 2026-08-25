class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def recurse(i, j):
            nonlocal s, p
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False
            
            if j + 1 < len(p) and p[j+1] == '*':
                memo[(i,j)] = False
                if i < len(s) and (p[j] == s[i] or p[j] == "."):
                    memo[(i,j)] = recurse(i+1, j+2) or recurse(i+1, j) or recurse(i, j+2)
                else:
                    memo[(i,j)] = recurse(i, j+2)
                return memo[(i,j)]
            
            if i < len(s) and s[i] == p[j] or p[j] == ".":
                memo[(i,j)] = recurse(i+1, j+1)
                return memo[(i,j)]


            memo[(i,j)] = False
            return False
        
        return recurse(0,0)