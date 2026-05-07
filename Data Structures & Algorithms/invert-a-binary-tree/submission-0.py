# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
                return None

        queue = []
        visited = []

        queue.append(root)
        visited.append(root)

        while queue:

            s = queue.pop(0)

            s.right, s.left = s.left, s.right

            if s.left and (s.left not in visited):
                queue.append(s.left)
                visited.append(s.left)

            if s.right and (s.right not in visited):
                queue.append(s.right)
                visited.append(s.right)

        return visited.pop(0)