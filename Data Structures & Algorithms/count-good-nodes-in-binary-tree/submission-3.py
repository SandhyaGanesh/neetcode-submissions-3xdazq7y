# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, maxSoFar = -101) -> int:
        if not root:
            return 0
        goodNodes = 0
        if root.val >= maxSoFar:
            goodNodes += 1
            maxSoFar = root.val
        return goodNodes + self.goodNodes(root.left, maxSoFar) + self.goodNodes(root.right, maxSoFar)