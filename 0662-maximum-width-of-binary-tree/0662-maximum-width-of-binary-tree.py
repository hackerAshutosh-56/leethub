# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        queue=deque([(root,0)])
        maxwidth=0
        while queue:
            size=len(queue)
            firstidx=queue[0][1]
            for i in range(size):
                node,index=queue.popleft()
                index=index-firstidx 
                if node.left:
                    queue.append((node.left,2*index))
                if node.right:
                    queue.append((node.right,2*index+1))
            maxwidth=max(maxwidth,index+1) 
        return maxwidth                      

        