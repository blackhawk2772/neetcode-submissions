"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
            nodes = {}

            def dfs(node):
                
                if node in nodes:
                    return nodes[node]
                
                if not node:
                    return None
                
                nodes[node] = Node()
                nodes[node].val = node.val
                
                for neighbor in node.neighbors:
                    nodes[node].neighbors.append(dfs(neighbor))
                
                return nodes[node]

            
            return dfs(node)



