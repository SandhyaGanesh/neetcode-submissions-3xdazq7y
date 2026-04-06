class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl = len(s)
        pl = len(p)

        dp = [[False]*(pl+1) for _ in range(sl+1)]

        dp[-1][-1] = True

        for i in range(sl-1, -1, -1):
            dp[i][-1] = False
        for j in range(pl-1, -1, -1):
            if p[j] == "*":
                continue
            dp[-1][j] = dp[-1][j+2] if (j+1 < pl and p[j+1] == "*") else False
        
        for i in range(sl-1, -1, -1):
            for j in range(pl-1, -1, -1):
                if p[j] == "*":
                    continue
                if s[i] == p[j] or p[j] == '.':
                    if j+1 < pl and p[j+1] == "*":
                        dp[i][j] = dp[i+1][j+2] or dp[i+1][j] or dp[i][j+2]
                    else:
                        dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = dp[i][j+2] if (j+1 < pl and p[j+1] == "*") else False
        
        return dp[0][0]
        
        # def dfs(i, j):
        #     if i == sl and j == pl:
        #         return True
            
        #     res = False
        #     if j+1 < pl and p[j+1] == "*":
        #         res = res or dfs(i, j+2)

        #     if i == sl or j == pl:
        #         return res
            
        #     # res = False
        #     if s[i] == p[j] or p[j] == '.':
        #         if j+1 < pl and p[j+1] == "*":
        #             res = res or dfs(i+1, j+2) or dfs(i+1, j)
        #         else:
        #             res = res or dfs(i+1, j+1)

        #     return res

        # return dfs(0,0)