class Solution:
    def getValidDirections(self, x, y, r, c):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result = []

        for dx, dy in directions:
            if 0 <= x + dx < r and 0 <= y + dy < c:
                result.append((x + dx, y + dy))
        
        return result

    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        res = 0
        
        def traverse(x, y):
            grid[x][y] = 'X'
            for nx, ny in self.getValidDirections(x, y, r, c):
                if grid[nx][ny] == '1':
                    traverse(nx, ny)

        for x in range(r):
            for y in range(c):
                if grid[x][y] == '1':
                    res += 1
                    traverse(x, y)
        return res