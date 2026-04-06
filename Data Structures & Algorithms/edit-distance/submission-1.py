class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        res = 0
        l1 = len(word1)
        l2 = len(word2)
        memo = {}
        
        def dfs(i, j):
            nonlocal res, word1, word2, l1, l2
            if (i,j) in memo:
                return memo[(i,j)]
            if i == l1 and j == l2:
                memo[(i,j)] = 0
                return 0
            if i == l1:
                memo[(i,j)] = l2 - j
                return l2 - j
            if j == l2:
                memo[(i,j)] = l1 - i
                return l1 - i
            
            if word1[i] == word2[j]:
                memo[(i,j)] = dfs(i+1, j+1)
                return memo[(i,j)]
            
            memo[(i,j)] = 1 + min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1))
            return memo[(i,j)]
            
        
        return dfs(0,0)