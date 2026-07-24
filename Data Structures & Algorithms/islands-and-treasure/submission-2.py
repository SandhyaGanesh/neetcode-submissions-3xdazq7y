class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r = len(grid)
        c = len(grid[0])

        def getNeighbors(x, y):
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            neighbors = []
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < r and 0 <= ny < c:
                    neighbors.append((nx, ny))
            
            return neighbors
        
        def traverse(x, y, distance):
            if grid[x][y] == -1:
                return
            grid[x][y] = min(grid[x][y], distance)

            for nx, ny in getNeighbors(x, y):
                if grid[nx][ny] > grid[x][y] + 1:
                    traverse(nx, ny, grid[x][y] + 1)
        
        for x in range(r):
            for y in range(c):
                if grid[x][y] == 0:
                    traverse(x, y, 0)
        
        return