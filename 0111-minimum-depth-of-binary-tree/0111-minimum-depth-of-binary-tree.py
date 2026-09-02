# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if node is None :
                return 0
            if node.left is None:
                return  height(node.right)+1
            if node.right is None:
                return height(node.left)+1        
            leftht=height(node.left)
            rightht=height(node.right)
            return min(leftht,rightht)+1
        return height(root)       