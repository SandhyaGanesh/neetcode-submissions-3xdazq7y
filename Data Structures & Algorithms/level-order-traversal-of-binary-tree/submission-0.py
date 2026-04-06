# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []
        while q:
            levelList = []
            l = len(q)
            for i in range(l):
                node = q.popleft()
                if not node:
                    continue
                levelList.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if levelList:
                res.append(levelList)
        return res
