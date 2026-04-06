# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            l = len(q)
            levelEnd = -101
            for i in range(l):
                node = q.popleft()
                if node:
                    levelEnd = node.val
                    q.append(node.left)
                    q.append(node.right)
            if levelEnd != -101:
                res.append(levelEnd)
        return res