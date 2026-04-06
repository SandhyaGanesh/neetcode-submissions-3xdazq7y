class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        for ix in range(r):
            for iy in range(c):
                if grid[ix][iy] == 0:
                    grid[ix][iy] = -1
                if grid[ix][iy] == 2:
                    grid[ix][iy] = 0
                if grid[ix][iy] == 1:
                    grid[ix][iy] = 9999
    
        def validNextSteps(ix, iy):
            nonlocal r, c
            nextSteps = []
            if ix - 1 >= 0 and grid[ix-1][iy] != -1:
                nextSteps.append((ix-1, iy))
            if ix + 1 < r and grid[ix+1][iy] != -1:
                nextSteps.append((ix+1, iy))
            if iy - 1 >= 0 and grid[ix][iy-1] != -1:
                nextSteps.append((ix, iy-1))
            if iy + 1 < c and grid[ix][iy+1] != -1:
                nextSteps.append((ix, iy+1))
            return nextSteps

        for ix in range(r):
            for iy in range(c):
                if grid[ix][iy] == 0:
                    visited = [[False]*c for _ in range(r)]
                    q = deque([(ix, iy)])
                    distance = 0
                    while q:
                        for _ in range(len(q)):
                            currx, curry = q.popleft()
                            if visited[currx][curry]:
                                continue
                            grid[currx][curry] = min(distance, grid[currx][curry])
                            visited[currx][curry] = True
                            for nextX, nextY in validNextSteps(currx, curry):
                                q.append((nextX, nextY))
                        distance += 1
        res = max([max(row) for row in grid])
        res = max(res, 0)
        print(grid)
        return res if res != 9999 else -1
        