class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            if node not in adjList:
                return True
            for neighbor in adjList[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        
        res = dfs(0, -1)
        print(adjList)
        if len(visited) != n:
            return False
        return res