# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.arr = []
    
    def traverse(self, node):
        if not node:
            return
        
        self.traverse(node.left)
        self.arr.append(node.val)
        self.traverse(node.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse(root)
        return self.arr[k-1]