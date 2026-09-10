# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def preorder(root):
            if root is None:
                return
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        count=0
        freq=[]
        result=[]
        for i in ans:
            freq.append(ans.count(i))
        for i in range(len(freq)):
            if freq[i]==max(freq):
                result.append(ans[i])
        return list(set(result))       
                