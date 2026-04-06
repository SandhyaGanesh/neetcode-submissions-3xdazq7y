class Solution:
    def getValidNeighbors(self, ix, iy, r, c):
        res = []
        if ix - 1 >= 0:
            res.append((ix-1, iy))
        if ix + 1 < r:
            res.append((ix+1, iy))
        if iy - 1 >= 0:
            res.append((ix, iy-1))
        if iy + 1 < c:
            res.append((ix, iy+1))
        return res

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        res = 0

        for ix in range(r):
            for iy in range(c):
                if grid[ix][iy] == 0:
                    continue
                area = 1
                grid[ix][iy] = 0
                q = deque([(ix,iy)])
                while q:
                    xLand, yLand = q.popleft()
                    print(xLand, yLand)
                    for neighbors in self.getValidNeighbors(xLand, yLand, r, c):
                        if grid[neighbors[0]][neighbors[1]] == 1:
                            area += 1
                            grid[neighbors[0]][neighbors[1]] = 0
                            q.append((neighbors[0], neighbors[1]))
                res = max(area, res)
        return res