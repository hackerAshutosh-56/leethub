# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def identical(p,q):
            if p is None and q is None :
                return True
            if p is None or q is None :
                return False
            if p.val!= q.val:
                return False
            return identical(p.left,q.left) and identical(p.right,q.right)
        def subtree(root, subroot):
            if root is None :
                return False
            if (root.val==subroot.val) and identical(root,subroot):
                return True
            return subtree(root.left,subroot) or subtree(root.right,subroot)
        return subtree(root,subRoot)                             
        