# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def goodNodes(self, root: TreeNode, m = -101) -> int:
        res = 0
        if not root:
            return 0
        if root.val >= m:
            res += 1
            m = root.val
        
        res += self.goodNodes(root.left, m)
        res += self.goodNodes(root.right, m)

        return res
        