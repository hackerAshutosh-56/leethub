# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        def build(arr):
            if len(arr)==0:
                return None
            root=TreeNode(arr[0])
            i=1
            while i<len(arr) and arr[i]<arr[0]:
                i=i+1
            root.left=build(arr[1:i])
            root.right=build(arr[i:])
            return root
        return build(preorder)           
        