# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue=deque([(root,None)])
        while queue:
            size=len(queue)
            x_parent=None
            y_parent=None
            for _ in range(size):
                node,parent=queue.popleft()
                if node.val==x:
                    x_parent=parent
                if node.val==y:
                    y_parent=parent
                if node.left:
                    queue.append((node.left,node))
                if node.right:
                    queue.append((node.right,node))
            if x_parent is not None  and  y_parent is not None :
                return x_parent!=y_parent 
            if x_parent is not None or y_parent is not None:
                return False
        return False                              
        