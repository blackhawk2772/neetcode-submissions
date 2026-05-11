# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False

        def solver(node, val):
            
            if val == targetSum and not (node.left or node.right):
                return True
            
            #if val > targetSum:
            #    return False
            
            
            a = b = False
            if node.left:
                val += node.left.val
                a = solver(node.left, val)
                val -= node.left.val
            

            if node.right:
                val += node.right.val
                b = solver(node.right, val)
                val -= node.right.val

            return (a or b)

        return solver(root, root.val)