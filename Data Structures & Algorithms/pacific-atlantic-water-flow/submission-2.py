class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])

        pacific = set()
        atlantic = set()

        result = []

        for x in range(r):
            pacific.add((x,0))
            atlantic.add((x,c-1))
        for y in range(c):
            pacific.add((0,y))
            atlantic.add((r-1,y))
        
        def getNeighbors(x, y):
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            neighbors = []

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < r and 0 <= ny < c and heights[nx][ny] <= heights[x][y]:
                    neighbors.append((nx, ny))
            return neighbors
        
        q = []
        for x in range(r):
            for y in range(c):
                q.append((heights[x][y], (x,y)))
        q.sort()

        def canReachBoth(x, y, path):
            path.add((x,y))
            nonlocal canReachPacific, canReachAtlantic
            if (x,y) in pacific:
                canReachPacific = True
            if (x,y) in atlantic:
                canReachAtlantic = True

            if canReachPacific and canReachAtlantic:
                return True

            for nx, ny in getNeighbors(x,y):
                if (nx, ny) not in path and canReachBoth(nx, ny, path):
                    return True
            
            return False
        
        for h, (x, y) in q:
            canReachPacific = False
            canReachAtlantic = False
            if canReachBoth(x, y, set()):
                result.append((x, y))

        return result