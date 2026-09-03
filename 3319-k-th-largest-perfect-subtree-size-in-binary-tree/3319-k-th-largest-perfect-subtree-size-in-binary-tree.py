# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def dfs(node):
            if node is None :
                return 0
            left=dfs(node.left)
            right=dfs(node.right)

            if left==-1 or right==-1 or left!=right:
                return -1

            height=left+1
            size=2**height-1
            ans.append(size)
            return height 
        dfs(root)
        ans.sort(reverse=True)
        if len(ans)<k:
            return -1
        return ans[k-1]              
        
        