# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        def func(root,s):
            if root is None:
                return None
            s=s+str(root.val)
            if root.left is None and root.right is None:
                ans.append(s)
                return
            s=s+"->"
            func(root.left,s)
            func(root.right,s)
        func(root,"")            
        return ans 