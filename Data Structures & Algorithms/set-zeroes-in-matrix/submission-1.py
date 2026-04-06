class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if str(matrix[i][j]) == "0":
                    for r in range(m):
                        matrix[r][j] = "X" if str(matrix[r][j]) != "0" else 0
                    for c in range(n):
                        matrix[i][c] = "X" if str(matrix[i][c]) != "0" else 0
        
        print(matrix)
        for i in range(m):
            for j in range(n):
                if str(matrix[i][j]) == "X":
                    matrix[i][j] = 0