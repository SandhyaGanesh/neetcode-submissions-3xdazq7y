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
            return node
        
        nodeMap = {}

        q = deque()
        q.append(node)

        while q:
            oldNode = q.popleft()
            if oldNode not in nodeMap:
                nodeMap[oldNode] = Node(oldNode.val)
            for neighbor in oldNode.neighbors:
                if neighbor not in nodeMap:
                    nodeMap[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                nodeMap[oldNode].neighbors.append(nodeMap[neighbor])
                    
        
        return nodeMap[node]