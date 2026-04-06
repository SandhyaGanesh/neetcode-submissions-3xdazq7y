"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        copyMap = {}

        q = deque([node])
        while q:
            n = q.popleft()
            if n in copyMap:
                continue
            copyMap[n] = Node(n.val)
            for neighbor in n.neighbors:
                q.append(neighbor)

        processed = {}
        q = deque([node])
        while q:
            n = q.popleft()
            newNode = copyMap[n]
            if newNode in processed:
                continue
            processed[newNode] = True
            for neighbor in n.neighbors:
                newNode.neighbors.append(copyMap[neighbor])
                q.append(neighbor)
        return copyMap[node]
        