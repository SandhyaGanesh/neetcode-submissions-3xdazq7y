class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r = len(grid)
        c = len(grid[0])

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

        def markDistance(ix, iy, distance, visited):
            if visited[ix][iy]:
                return 
            grid[ix][iy] = min(distance, grid[ix][iy])
            visited[ix][iy] = True
            for nextX, nextY in validNextSteps(ix, iy):
                markDistance(nextX, nextY, distance+1, visited)

        for ix in range(r):
            for iy in range(c):
                if grid[ix][iy] == 0:
                    visited = [[False]*c for _ in range(r)]
                    #markDistance(ix, iy, 0, visited)
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
                        
        
        return
        