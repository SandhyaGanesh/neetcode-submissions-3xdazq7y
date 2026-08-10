class Solution:
    def __init__(self):
        self.graph = {}

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if n == 1:
            return 0
        for i in range(1, n+1):
            self.graph[i] = []
        for s, d, t in times:
            self.graph[s].append((d, t))
        
        q = deque([(k,0)])
        visited = {}

        while q:
            l = len(q)
            for _ in range(l):
                d, t = q.popleft()
                if (d in visited and visited[d] <= t):
                    continue
                visited[d] = t
                for nexd, nexte in self.graph[d]:
                    q.append((nexd, t+nexte))
        
        for i in range(1, n+1):
            if i not in visited:
                visited[i] = -1
        times = [visited[d] for d in visited]
        # print(visited)
        # print(times)
        return max(times) if min(times) != -1 else -1 