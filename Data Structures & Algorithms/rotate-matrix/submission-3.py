class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for layer in range(n//2):
            for i in range(n - 2*layer - 1):
                s1 = matrix[layer][i]
                s2 = matrix[i][n - layer - 1]
                s3 = matrix[n - layer - 1][n - layer - 1 - i]
                s4 = matrix[n - layer - 1 - i][layer]

                matrix[i][n - layer - 1] = s1
                matrix[n - layer - 1][n - layer - 1 - i] = s2
                matrix[n - layer - 1 - i][layer] = s3
                matrix[layer][i] = s4
                print(s1, s2, s3, s4)
        
        return