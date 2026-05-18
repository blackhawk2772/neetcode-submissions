
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        q = deque()
        q.append(node)
        visited = {node: Node(node.val)}
        

        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                # Link the cloned nodes here
                visited[curr].neighbors.append(visited[neighbor])
                        
        return visited[node]