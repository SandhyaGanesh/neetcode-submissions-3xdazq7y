class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        maxArea = 0

        def getNextSquares(x, y):
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            nextSquares = []

            for dx, dy in directions:
                nx = dx + x
                ny = dy + y
                if 0 <= nx < r and 0 <= ny < c:
                    nextSquares.append((nx, ny))
            
            return nextSquares
            
        def traverse(x, y):
            nonlocal area
            grid[x][y] = 'X'

            for nx, ny in getNextSquares(x, y):
                if grid[nx][ny] == 1:
                    traverse(nx, ny)
            
            area += 1
        
        for x in range(r):
            for y in range(c):
                area = 0
                if grid[x][y] == 1:
                    traverse(x,y)
                maxArea = max(maxArea, area)
        
        return maxArea