# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node):

            if node.val == p.val or node.val == q.val:
                return node

            f1 = f2 = None
            if node.left:
                f1 = dfs(node.left)        
            if node.right:
                f2 = dfs(node.right)
            
            if f1 and f2:
                return node
            else:
                return (f1 or f2)
        
        return dfs(root)