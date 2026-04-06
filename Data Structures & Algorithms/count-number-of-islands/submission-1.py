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

    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])

        res = 0

        for ix in range(r):
            for iy in range(c):
                if grid[ix][iy] == "0":
                    continue
                grid[ix][iy] = "0"
                q = deque([(ix,iy)])
                while q:
                    xLand, yLand = q.popleft()
                    for neighbors in self.getValidNeighbors(xLand, yLand, r, c):
                        if grid[neighbors[0]][neighbors[1]] == "1":
                            grid[neighbors[0]][neighbors[1]] = "0"
                            q.append((neighbors[0], neighbors[1]))
                res += 1
        return res