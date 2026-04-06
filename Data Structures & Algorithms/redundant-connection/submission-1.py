class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        degree = [0 for _ in range(n + 1)]
        adjList = {}
        visited = set()
        for i in range(1,n + 1):
            adjList[i] = []
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
            degree[src] += 2
            degree[dst] += 2
        
        q = deque()
        for node in range(1, n+1):
            if degree[node] == 2:
                q.append(node)
        
        while q:
            node = q.popleft()
            degree[node] -= 2
            visited.add(node)
            for neighbor in adjList[node]:
                degree[neighbor] -= 2
                if neighbor not in visited and degree[neighbor] == 2:
                    q.append(neighbor)
        
        cycleNodes = set()
        for node in range(1, n+1):
            if degree[node] > 0:
                cycleNodes.add(node)
        print(degree)
        print(cycleNodes)
        edges = edges[::-1]
        for src, dst in edges:
            if src in cycleNodes and dst in cycleNodes:
                return [src,dst]
        return []