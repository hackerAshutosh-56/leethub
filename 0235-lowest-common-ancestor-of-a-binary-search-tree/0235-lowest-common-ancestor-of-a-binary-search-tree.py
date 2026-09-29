# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        def lca(root,p,q):
            if root is None :
                return None
            if root==p or root==q:
                return root
            left=lca(root.left,p,q)
            right=lca(root.right,p,q)
            if left!=None and right!=None:
                return root
            if left:
                return left 
            if right:
                return right
        return lca(root,p,q)     """

        # BST APPROACH
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root
        
                  

        