class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        maxLen = max(l1, l2)
        memo = {}

        def recurse(i, j, cost):
            if (i,j,cost) in memo:
                return memo[(i,j,cost)]
            if i == l1 and j == l2:
                return cost
            if i == l1:
                return l2 - j + cost
            if j == l2:
                return l1 - i + cost
            
            if word1[i] == word2[j]:
                return recurse(i+1, j+1, cost)
            c1 = recurse(i+1, j, cost+1)
            c2 = recurse(i, j+1, cost+1)
            c3 = recurse(i+1, j+1, cost+1)

            memo[(i,j,cost)] = min(c1,c2,c3)
            return memo[(i,j,cost)]
        
        return recurse(0,0,0)


        