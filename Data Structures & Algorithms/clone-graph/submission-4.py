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

        def getNewNode(n):
            if n in copyMap:
                return copyMap[n]
            
            newNode = Node(n.val)
            copyMap[n] = newNode
            for neighbor in n.neighbors:
                copyMap[n].neighbors.append(getNewNode(neighbor))
            return newNode
        
        copyMap[node] = getNewNode(node)
        return copyMap[node]
        