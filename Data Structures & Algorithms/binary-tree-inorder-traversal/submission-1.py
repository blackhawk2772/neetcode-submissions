# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack =  []

        def helper(node: TreeNode, stack: []):
            
            if node.left:
                helper(node.left, stack)

            stack.append(node.val)

            if node.right:
                helper(node.right, stack)    

        if not root:
            return []

        helper(root, stack)

        return stack


