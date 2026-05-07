# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:



        def helper(root: TreeNode, depth):
            nonlocal maximum

            l,r = 0, 0

            if root.left:
                l += helper(root.left, depth+1) 

            if root.right:
                r += helper(root.right, depth+1)

            if (l + r ) > maximum:
                maximum = (l + r )

            return 1+max(l,r)
        
        maximum = 0
        
        helper(root, 0)

        return maximum