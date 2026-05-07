# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node: TreeNode, maximum: int, count: int):

            if not node:
                return count

            if node.val > maximum: maximum = node.val

            if maximum <= node.val: count +=1
            
            if node.left:
                count = helper(node.left, maximum, count)

            if node.right:
                count = helper(node.right, maximum, count)
            
            return count
        
        return helper(root, root.val, 0)