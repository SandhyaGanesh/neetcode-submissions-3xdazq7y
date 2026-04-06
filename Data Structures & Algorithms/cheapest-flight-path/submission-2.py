class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = {}
        res = float("inf")
        for i in range(n):
            adjList[i] = []
        for s, d, c in flights:
            adjList[s].append((c,d))
        
        q = deque()
        q.append((src, 0))

        while k+2:
            l = len(q)
            for i in range(l):
                node, runningCost = q.popleft()
                if node == dst:
                    res = min(runningCost, res)
                for c, airport in adjList[node]:
                    q.append((airport, c+runningCost))
            k -= 1
        
        return res if res != float("inf") else -1
                