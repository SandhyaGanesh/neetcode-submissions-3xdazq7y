class Solution:
    def __init__(self):
        self.res = []

    def isPalindrome(self, s: str):
        i = 0
        e = len(s) - 1
        while i <= e:
            if s[i] != s[e]:
                return False
            i += 1
            e -= 1
        
        return True

    def recurse(self, s: str, i: int, path: List[str]) -> List[str]:
        if i == len(s):
            self.res.append(path[:])
            return
        
        for j in range(i, len(s)):
            c = s[i:j+1]
            self.recurse(s, j+1, path + [c])
            
    def partition(self, s: str) -> List[List[str]]:
        self.recurse(s, 0, [])
        newRes = []
        
        for wordList in self.res:
            flag = True
            for word in wordList:
                if not self.isPalindrome(word):
                    flag = False
                    break
            if flag:
                newRes.append(wordList)
        return newRes

