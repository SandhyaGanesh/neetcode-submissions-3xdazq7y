class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
    
    def getNeighbors(self, i,j):
        ret = []
        if 0 <= j-1 < self.n:
            ret.append((i,j-1))
        if 0 <= j+1 < self.n:
            ret.append((i,j+1))
        if 0 <= i-1 < self.m:
            ret.append((i-1,j))
        if 0 <= i+1 < self.m:
            ret.append((i+1,j))
        return ret    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        ret = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "0":
                    continue
                q = deque([(i,j)])
                while q:
                    x,y = q.popleft()
                    grid[x][y] = "0"
                    for nx, ny in self.getNeighbors(x,y):
                        if grid[nx][ny] == "1":
                            q.append((nx, ny))
                ret += 1
        return ret

