class Solution:
    def getNeighbors(self, x, y, n):
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        neighbors = []
        for dx, dy in directions:
            if 0 <= x + dx < n and 0 <= y + dy < n:
                neighbors.append((x+dx, y+dy))
        return neighbors

    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = []
        heapq.heappush(heap, (0, (0,0), grid[0][0]))
        t = 0
        visited = set()
        while heap:
            tupl = heapq.heappop(heap)
            pathMax, x, y, v = tupl[0], tupl[1][0], tupl[1][1], tupl[2]
            if (x, y) in visited:
                continue
            visited.add((x, y))

            pathMax = max(pathMax, v)
            if x == n-1 and y == n-1:
                return pathMax
            for nx, ny in self.getNeighbors(x, y, n):
                if (nx, ny) not in visited:
                    newPathMax = max(pathMax, grid[nx][ny])
                    heapq.heappush(heap, (newPathMax, (nx, ny), grid[nx][ny]))
            if v <= t:
                t += 1
            else:
                t = v


        return 0