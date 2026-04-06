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
    
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        maxArea = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    continue
                area = 0
                q = deque([(i,j)])
                print("i---j",i,j)
                while q:
                    x,y = q.popleft()
                    if grid[x][y] == 0:
                        continue
                    grid[x][y] = 0
                    print(x,y)
                    area += 1
                    for nx, ny in self.getNeighbors(x,y):
                        if grid[nx][ny] == 1:
                            q.append((nx, ny))
                maxArea = max(area, maxArea)
        return maxArea

