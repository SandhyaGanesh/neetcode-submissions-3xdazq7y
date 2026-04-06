class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        
        adjList = {}
        minHeap = []
        for i in range(len(points)):
            p1x, p1y = points[i]
            adjList[(p1x, p1y)] = []
            for j in range(len(points)):
                if points[i] == points[j]:
                    continue
                p2x, p2y = points[j]
                cost = abs(p1x-p2x)+abs(p1y-p2y)
                adjList[(p1x, p1y)].append((cost, (p2x, p2y)))
        
        print(adjList)
        cost = 0
        visited = set([(points[0][0], points[0][1])])
        minHeap = []
        print("popped: ", (points[0][0], points[0][1]))
        for edge in adjList[(points[0][0], points[0][1])]:
            print(edge)
            heapq.heappush(minHeap, edge)
        
        while len(visited) < len(points):
            c, p = heapq.heappop(minHeap)
            
            if p not in visited:
                #print(cost, c , p)
                cost += c
                print("popped: ", p)
                for edge in adjList[(p[0], p[1])]:
                    print(edge)
                    heapq.heappush(minHeap, edge)
                visited.add(p)

        
        return cost

