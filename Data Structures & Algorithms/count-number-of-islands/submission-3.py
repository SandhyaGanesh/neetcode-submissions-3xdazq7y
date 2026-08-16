class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        numIslandRes = 0

        def getNeighbors(x, y):
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            neighbors = []
            for dx, dy in directions:
                if 0 <= x + dx < r and 0 <= y + dy < c:
                    neighbors.append((x+dx, y+dy))
            return neighbors
        
        def traverse(x, y):
            if grid[x][y] != "1":
                return
            grid[x][y] = "X"
            for nx, ny in getNeighbors(x, y):
                traverse(nx, ny)
            return

        for x in range(r):
            for y in range(c):
                if grid[x][y] == "1":
                    traverse(x, y)
                    numIslandRes += 1
        
        return numIslandRes