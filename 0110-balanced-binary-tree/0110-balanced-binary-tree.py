# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            leftht=height(node.left)
            rightht=height(node.right)
            if leftht==-1 or rightht==-1:
                return -1
            if abs(leftht-rightht)>1:
                return -1
            return max(leftht,rightht)+1
        if height(root)!=-1:
            return True
        else:
            return False                