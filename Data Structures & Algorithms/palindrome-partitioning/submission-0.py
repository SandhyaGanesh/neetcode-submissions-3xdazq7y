class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        l = len(s)

        def helper(index, path):
            if index == l:
                res.append(path[:])
                return
            
            for i in range(index+1, l+1):
                path.append(s[index:i])
                helper(i, path)
                path.pop()
        
        def isPalindrome(s):
            i = 0
            e = len(s) - 1
            while i <= e:
                if s[i] != s[e]:
                    return False
                i += 1
                e -= 1
            return True

        helper(0, [])
        res2 = []
        
        for r in res:
            notPal = False
            for w in r:
                if not isPalindrome(w):
                    notPal = True
                    break
            if not notPal:
                res2.append(r)
        return res2
        

        