# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        answer =  True

        def helper(node: TreeNode, depth: int):
            nonlocal answer
            if not node:
                if depth > maxim:
                    maxim = depth

                if depth < minim:
                    minim =  depth
                
                return depth

            l,r = depth, depth

            if node.left: 
                l = helper(node.left,depth+1)
                
            if node.right:
                r = helper(node.right,depth+1)    
            
            if abs(l-r) > 1:
                answer = False

            return max(l,r)
                 
        if not root:
            return True

        depth = 0
        helper(root, depth)
        return answer

