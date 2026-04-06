class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adjList = {}
        for i in range(n):
            adjList[i] = []
        
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        components = 0
        unvisited = set([i for i in range(n)])
        def dfs(node):
            if node not in unvisited:
                return
            unvisited.remove(node)
            for neighbor in adjList[node]:
                dfs(neighbor)
        
        while True:
            if len(unvisited) == 0:
                break
            i = unvisited.pop()
            unvisited.add(i)
            dfs(i)
            components += 1
        
        return components