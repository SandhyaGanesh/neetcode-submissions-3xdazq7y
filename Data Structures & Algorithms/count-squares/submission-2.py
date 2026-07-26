class CountSquares:

    def __init__(self):
        self.pointMap = {}
        self.xAxisMap = {}
        self.yAxisMap = {}

    def add(self, point: List[int]) -> None:
        self.pointMap[tuple(point)] = self.pointMap.get(tuple(point), 0) + 1
        x = point[0]
        y = point[1]
        self.xAxisMap[x] = self.xAxisMap.get(x, set())
        self.xAxisMap[x].add(tuple(point))
        self.yAxisMap[y] = self.yAxisMap.get(y, set())
        self.yAxisMap[y].add(tuple(point))

    def count(self, point: List[int]) -> int:
        squares = 0
        x = point[0]
        y = point[1]

        xPoints = self.xAxisMap.get(x, set())
        yPoints = self.yAxisMap.get(y, set())

        for nx, ny in xPoints:
            if x == nx and y == ny:
                continue
            l = abs(y - ny)
            if (x - l, y) in self.pointMap and (x - l, ny) in self.pointMap:
                squares += self.pointMap[(nx, ny)]*self.pointMap[(x - l, y)]*self.pointMap[(x - l, ny)]
            if (x + l, y) in self.pointMap and (x + l, ny) in self.pointMap:
                squares += self.pointMap[(nx, ny)]*self.pointMap[(x + l, y)]*self.pointMap[(x + l, ny)]
        
        return squares

