class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        l = max(l1, l2)
        if l1 < l2:
            text1 += '.'*(l-l1)
        elif l2 < l1:
            text2 += '.'*(l-l2)
        
        subsequenceDP = [[0]*l for _ in range(l)]

        for i in range(l):
            subsequenceDP[0][i] = max(subsequenceDP[0][i-1] if i > 0 else 0, 1 if text1[0] == text2[i] else 0)
            subsequenceDP[i][0] = max(subsequenceDP[i-1][0] if i > 0 else 0, 1 if text1[i] == text2[0] else 0)
        
        for subsequence in subsequenceDP:
            print(subsequence)
        for i in range(1,l):
            for j in range(1,l):
                if text1[i] == text2[j]:
                    subsequenceDP[i][j] = 1 + subsequenceDP[i-1][j-1]
                else:
                    subsequenceDP[i][j] = max(subsequenceDP[i][j-1], subsequenceDP[i-1][j])
        
        return subsequenceDP[-1][-1]