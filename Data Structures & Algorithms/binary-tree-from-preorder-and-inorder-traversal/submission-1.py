# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        print(preorder)
        if not preorder:
            return None
        
        rootVal = preorder[0]
        i = 0
        while i < len(preorder) and rootVal != inorder[i]:
            i += 1
        
        rootNode = TreeNode(rootVal)
        print("left", preorder[1:i+1])
        rootNode.left = self.buildTree(preorder[1:i+1], inorder[:i])
        print("right", preorder[i+1:])
        rootNode.right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return rootNode
