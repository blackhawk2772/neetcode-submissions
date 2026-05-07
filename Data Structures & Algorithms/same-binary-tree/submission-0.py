# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        out1 = []
        out2 = []

        def helper(node: TreeNode, out: []):
            
            if not node:       
                return out

            out.append(node.val) 
            
            if not node.left:
                out.append(None)
            else:
                helper(node.left,out)
            
            if not node.right:
                out.append(None)
            else:
                helper(node.right,out)

            return out

        if helper(p,out1) == helper(q,out2):
            return True
        else:
            return False
        