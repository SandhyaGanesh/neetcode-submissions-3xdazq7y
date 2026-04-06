class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            return matrix[0]
        if n == 1:
            return [row[0] for row in matrix]
        
        levels = min(n,m) // 2
        spiralOrder = []
        for level in range(levels):
            for j in range(level, n - level):
                spiralOrder.append(matrix[level][j])
            for i in range(level + 1, m - level - 1):
                spiralOrder.append(matrix[i][n - level - 1])
            for j in range(n - level - 1, level - 1, -1):
                spiralOrder.append(matrix[m - level - 1][j])
            for i in range(m - level - 2, level, -1):
                spiralOrder.append(matrix[i][level])
        if m <= n:
            if m%2 == 1:
                spiralOrder.extend(matrix[m//2][levels:-levels])
        else:
            if n%2 == 1:
                spiralOrder.extend([row[n//2] for row in matrix[levels:-levels]])

        return spiralOrder