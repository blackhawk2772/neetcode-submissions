# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        stack = []

        stack.append((root,1))

        maximum = 1

        while stack:
            
            s, d = stack.pop()

            if d>maximum:
                maximum = d

            if s.right:
                stack.append((s.right,d+1))

            if s.left:
                stack.append((s.left,d+1))

        return maximum