
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        q = deque()
        q.append(node)
        visited = {node: Node(node.val)}

        while q:
            root = q.popleft()
            for neighbor in root.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                # Link the cloned nodes here
                visited[root].neighbors.append(visited[neighbor])
                        
        return visited[node]