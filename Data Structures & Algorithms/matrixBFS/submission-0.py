class Solution:
    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0

    def validNeighbors(self, node):
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        neigbors = []
        x = node[0]
        y = node[1]
        for xd, yd in directions:
            if (0 <= x+xd < self.rows and 
                0 <= y+yd < self.cols and
                self.grid[x+xd][y+yd] != 1):
                neigbors.append((x+xd, y+yd))
        return neigbors

    def shortestPath(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        q = deque()
        visited = set()
        level = 0

        q.append((0,0))
        visited.add((0,0))

        while q:
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                visited.add(node)

                if node == (self.rows - 1, self.cols - 1):
                    return level

                for neighbor in self.validNeighbors(node):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            level += 1
        return -1


        