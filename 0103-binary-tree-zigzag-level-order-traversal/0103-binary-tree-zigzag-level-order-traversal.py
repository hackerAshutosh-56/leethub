# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        q=deque()
        result=[] 
        q.append(root)
        direction=True
        while q:
            n=len(q)
            ans=[]
            for i in range (n):
                node=q.popleft()
                ans.append(node.val)
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
            if direction is True:
                result.append(ans)
                direction=False
            else:
                ans.reverse()
                result.append(ans)
                direction=True
        return result        


        