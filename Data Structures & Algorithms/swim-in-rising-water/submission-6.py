class Solution:
    def getNeighbors(self, x, y, r, c):
        directions = [(1,0), (0,1), (-1, 0), (0, -1)]
        neighbors = []
        for dx, dy in directions:
            if 0 <= dx + x < r and 0 <= dy + y < c:
                neighbors.append((x + dx, y + dy))
        return neighbors
    
    def swimInWater(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        adjList = {}
        costs = []
        pathMaxMap = {}

        for ix in range(r):
            for iy in range(c):
                pathMaxMap[(ix, iy)] = float("inf")
                adjList[(ix, iy)] = []
                for nx, ny in self.getNeighbors(ix, iy, r, c):
                    adjList[(ix, iy)].append((nx, ny))
        
        minHeap = []
        heapq.heappush(minHeap, (grid[0][0], (0,0)))
        while minHeap:
            pathMax, (ix, iy) = heapq.heappop(minHeap)
            if ix == r - 1 and iy == c - 1:
                costs.append(pathMax)
            for nx, ny in adjList[(ix, iy)]:
                if pathMax >= pathMaxMap[(nx, ny)]:
                    continue
                pathMaxMap[(nx, ny)] = pathMax
                heapq.heappush(minHeap, (max(pathMax, grid[nx][ny]), (nx,ny)))
        return min(costs)