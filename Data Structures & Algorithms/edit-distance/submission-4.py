class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        maxLen = max(l1, l2)
        memo = {}

        def recurse(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == l1 and j == l2:
                return 0
            if i == l1:
                return l2 - j
            if j == l2:
                return l1 - i
            
            if word1[i] == word2[j]:
                return recurse(i+1, j+1)
            c1 = recurse(i+1, j)
            c2 = recurse(i, j+1)
            c3 = recurse(i+1, j+1)

            memo[(i,j)] = min(c1,c2,c3) + 1
            return memo[(i,j)]
        
        return recurse(0,0)


        