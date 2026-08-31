# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """  # o(n**2)
        def height(root):
            if root is None :
                return 0
            leftht=height(root.left)
            rightht=height(root.right)
            return max(leftht,rightht)+1
        def diameter(root):
            if root is None:
                return 0
            leftdia=diameter(root.left)
            rightdia=diameter(root.right)
            currentdia=height(root.left)+height(root.right)
            return max(leftdia,rightdia,currentdia)
        return diameter(root)      
        """
        ans=0
        def height(root):
            nonlocal ans
            if root is None:
                return 0
            leftht=height(root.left)
            rightht=height(root.right)
            ans=max(ans,leftht+rightht)
            return max(leftht,rightht)+1
        height(root)
        return ans
        