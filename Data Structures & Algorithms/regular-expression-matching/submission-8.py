class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl = len(s)
        pl = len(p)
        
        def dfs(i, j):
            print(i, sl, j, pl)
            if i == sl and j == pl:
                print("Returning True, ", i, j)
                return True
            
            res = False
            if j+1 < pl and p[j+1] == "*":
                res2 = dfs(i, j+2)
                print("Calling dfs(i, j+2): ", i, j+2)
                res = res or res2

            if i == sl or j == pl:
                print("Returning res, ", res, i, j)
                return res
            
            if s[i] == p[j] or p[j] == '.':
                if j+1 < pl and p[j+1] == "*":
                    res2 = dfs(i+1, j+2)
                    print("Calling dfs(i+1, j+2): ", i+1, j+2)
                    res = res or res2
                else:
                    res2 = dfs(i+1, j+1)
                    print("Calling dfs(i+1, j+1): ", i+1, j+1)
                    res = res or res2
            
                if j+1 < pl and p[j+1] == "*":
                    res2 = dfs(i+1, j)
                    print("Calling dfs(i+1, j): ", i+1, j)
                    res = res or res2

            print("Returning res, ", res, i, j)
            return res

        return dfs(0,0)