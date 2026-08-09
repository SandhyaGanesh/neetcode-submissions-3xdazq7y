class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # for row in matrix:
        #     print(row)
        for layer in range(n//2):
            for i in range(layer, n-layer-1):
                c1 = matrix[layer][i]
                c2 = matrix[i][n-layer-1]
                c3 = matrix[n-layer-1][n-1-i]
                c4 = matrix[n-1-i][layer]

                matrix[i][n-layer-1] = c1
                matrix[n-layer-1][n-1-i] = c2
                matrix[n-1-i][layer] = c3
                matrix[layer][i] = c4
        #print("#######")
        # for row in matrix:
        #     print(row)
                