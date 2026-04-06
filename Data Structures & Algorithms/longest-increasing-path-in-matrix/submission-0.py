class Solution:
    def getNeighbors(self, ix, iy, r, c):
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        neighbors = []
        for dx, dy in directions:
            if 0 <= ix+dx < r and 0 <= iy+dy < c:
                neighbors.append((ix+dx, iy+dy))
        return neighbors
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        dp = [[1]*c for _ in range(r)]

        q = []
        for i in range(r):
            for j in range(c):
                heapq.heappush(q, (-1*matrix[i][j], (i,j)))
        
        while q:
            val, (x, y) = heapq.heappop(q)
            for nx, ny in self.getNeighbors(x, y, r, c):
                if matrix[nx][ny] > matrix[x][y]:
                    dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
        
        return max([max(row) for row in dp])