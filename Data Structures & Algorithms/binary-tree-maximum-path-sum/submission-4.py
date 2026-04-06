# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepthSum(self, root: Optional[TreeNode], l={}) -> int:
        if not root:
            return 0
        if root in l:
            return l[root]
        print("In maxDepthSum: ", root.val)
        lSum = self.maxDepthSum(root.left)
        rSum = self.maxDepthSum(root.right)
        
        l[root] = max(lSum, rSum, 0) + root.val
        return l[root]

        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1000001

        print("In maxPathSum: ", root.val)
        lSum = self.maxPathSum(root.left)
        rSum = self.maxPathSum(root.right)

        l = self.maxDepthSum(root.left)
        r = self.maxDepthSum(root.right)
        iSum = max(l, l + r, r, 0) + root.val

        return max(lSum, iSum, rSum)