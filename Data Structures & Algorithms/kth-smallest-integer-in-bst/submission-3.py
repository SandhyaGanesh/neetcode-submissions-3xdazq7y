# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kCounter = [0]
        res = [root.val]
        def inOrderTraversal(root):
            if not root:
                return 
            
            inOrderTraversal(root.left)
            kCounter[0] += 1
            if kCounter[0] == k:
                res[0] = root.val
            inOrderTraversal(root.right)
        
        inOrderTraversal(root)
        return res[0]
        