# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = deque()
        res = []        
        queue.append(root)

        while queue:
            length = len(queue)
            cur = []
            for i in range(length):
                node = queue.popleft()
                if node:
                    cur.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if cur:
                res.append(cur)
        return res