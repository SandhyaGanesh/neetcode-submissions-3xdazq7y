class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for layer in range(n//2):
            for i in range(n - 2*layer - 1):
                s1 = matrix[layer][i + layer]
                s2 = matrix[i + layer][n - layer - 1]
                s3 = matrix[n - layer - 1][n - layer - 1 - i]
                s4 = matrix[n - layer - 1 - i][layer]

                matrix[i + layer][n - layer - 1] = s1
                matrix[n - layer - 1][n - layer - 1 - i] = s2
                matrix[n - layer - 1 - i][layer] = s3
                matrix[layer][i + layer] = s4        
        
        return