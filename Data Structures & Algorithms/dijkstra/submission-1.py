class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjList = {}
        for s, d, c in edges:
            t = adjList.get(s, [])
            t.append((d, c))
            adjList[s] = t
        
        dist = {}
        for i in range(n):
            dist[i] = float("inf")
        
        minHeap = []
        heapq.heappush(minHeap, (0, src))
        while minHeap:
            c, node = heapq.heappop(minHeap)
            if c >= dist[node]:
                continue
            dist[node] = c
            if node not in adjList:
                continue
            for d, cost in adjList[node]:
                heapq.heappush(minHeap, (c+cost, d))
        
        for e in dist.keys():
            if dist[e] == float("inf"):
                dist[e] = -1
        return dist

