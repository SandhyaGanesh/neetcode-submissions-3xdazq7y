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
            return ""
        
        result = []
        q = deque()
        q.append(root)
        isNodePresent = True
        while q and isNodePresent:
            l = len(q)
            isNodePresent = False
            for _ in range(l):
                node = q.popleft()
                result.append(node.val)
                if node.val == -1001:
                    continue
                if node.left or node.right:
                    isNodePresent = True
                if node.left:
                    q.append(node.left)
                else:
                    q.append(TreeNode(-1001))
                if node.right:
                    q.append(node.right)
                else:
                    q.append(TreeNode(-1001))
        result = [str(r) for r in result]
        return ','.join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        result = data.split(',')
        result = [int(r) for r in result]
        result.reverse()
        print(result)
        root = TreeNode(result.pop())
        q = deque()
        q.append(root)
        while result:
            node = q.popleft()
            l = result.pop()
            if l != -1001:
                node.left = TreeNode(l)
                q.append(node.left)
            r = result.pop()
            if r != -1001:
                node.right = TreeNode(r)
                q.append(node.right)
        return root
