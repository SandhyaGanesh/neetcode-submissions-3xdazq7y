# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        
        print(res)
        return ','.join(res)
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(',')
        l = len(res)
        if l == 1:
            return None

        nodeList = [None if c == 'N' else TreeNode(int(c)) for c in res]

        rootPtr = 0
        childPtr = 1
        while childPtr < l:
            root = nodeList[rootPtr]
            if root:
                root.left = nodeList[childPtr]
                print(root.left.val if root.left else "none")
                childPtr += 1
                root.right = nodeList[childPtr]
                print(root.right.val if root.right else "none")
                childPtr += 1
            
            rootPtr += 1
            
        return nodeList[0]
