class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        for x in range(r):
            for y in range(c):
                if grid[x][y] == 2:
                    grid[x][y] = 'X'
                if grid[x][y] == 1:
                    grid[x][y] = 'F'

        def getNeighbors(x, y):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            neighbors = []

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < r and 0 <= ny < c:
                    neighbors.append((nx, ny))
            
            return neighbors
        
        def bfs(x, y):
            q = deque()
            q.append((x,y))
            distance = 0

            while q:
                l = len(q)
                for _ in range(l):
                    px, py = q.popleft()
                    if grid[px][py] != 'X':
                        grid[px][py] = distance
                    for nx, ny in getNeighbors(px, py):
                        if grid[nx][ny] != 'X' and grid[nx][ny] != 0:
                            if grid[nx][ny] == 'F' or grid[nx][ny] > distance + 1:
                                q.append((nx, ny))
                distance += 1

        
        for x in range(r):
            for y in range(c):
                if grid[x][y] == 'X':
                    bfs(x, y)
        
        for x in range(r):
            for y in range(c):
                if grid[x][y] == 'X':
                    grid[x][y] = -1
                if grid[x][y] == 'F':
                    return -1
        
        maxDist = 0
        for x in range(r):
            for y in range(c):
                maxDist = max(maxDist, grid[x][y])
        return maxDist