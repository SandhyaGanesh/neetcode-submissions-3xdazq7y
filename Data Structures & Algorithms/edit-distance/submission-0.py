class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        res = 0
        l1 = len(word1)
        l2 = len(word2)
        
        def dfs(i, j):
            nonlocal res, word1, word2, l1, l2
            if i == l1 and j == l2:
                return 0
            if i == l1:
                return l2 - j
            if j == l2:
                return l1 - i
            
            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            
            return 1 + min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1))

            
        
        return dfs(0,0)