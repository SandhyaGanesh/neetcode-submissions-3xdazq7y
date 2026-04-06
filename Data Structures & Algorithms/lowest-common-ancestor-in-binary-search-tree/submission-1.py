# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getPath(self, root, n, path):
        path.append(root)
        if root.val == n:
            return path
        if root.val > n:
            return self.getPath(root.left, n, path)
        else:
            return self.getPath(root.right, n, path)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p1 = self.getPath(root, p.val, [])
        p2 = self.getPath(root, q.val, [])
        for p in p1:
            print(p.val)
        print("hey")
        for p in p2:
            print(p.val)
        
        if len(p1) > len(p2):
            p2.extend([None]*(len(p1) - len(p2)))
        if len(p1) < len(p2):
            p1.extend([None]*(len(p2) - len(p1)))
        m = min(len(p1),len(p2))
        if m == 1:
            return p1[0]
        for i in range(m):
            if p1[i] != p2[i]:
                return p1[i-1]
