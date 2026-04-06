class Solution:
    def getNeighbors(self, ix, iy, r, c):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dx, dy in directions:
            if 0 <= ix+dx < r and 0 <= iy+dy < c:
                neighbors.append((ix+dx, iy+dy))
        return neighbors
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])
        canReachPacific = [[False]*c for _ in range(r)]
        canReachAtlantic = [[False]*c for _ in range(r)]

        q = deque()
        for iy in range(c):
            canReachPacific[0][iy] = True
            q.append((0, iy))
        for ix in range(r):
            canReachPacific[ix][0] = True
            q.append((ix, 0))
        
        while q:
            ix, iy = q.popleft()
            for nx, ny in self.getNeighbors(ix, iy, r, c):
                if not canReachPacific[nx][ny] and heights[ix][iy] <= heights[nx][ny]:
                    canReachPacific[nx][ny] = True
                    q.append((nx, ny))
        
        q = deque()
        for iy in range(c):
            canReachAtlantic[r-1][iy] = True
            q.append((r-1, iy))
        for ix in range(r):
            canReachAtlantic[ix][c-1] = True
            q.append((ix, c-1))
        
        while q:
            ix, iy = q.popleft()
            for nx, ny in self.getNeighbors(ix, iy, r, c):
                if not canReachAtlantic[nx][ny] and heights[ix][iy] <= heights[nx][ny]:
                    canReachAtlantic[nx][ny] = True
                    q.append((nx, ny))
        
        res = []
        for ix in range(r):
            for iy in range(c):
                if canReachPacific[ix][iy] and canReachAtlantic[ix][iy]:
                    res.append([ix, iy])
        
        return res
        