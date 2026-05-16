class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [ i for i in range(n)]
        size = [1] * n
        groups = n

        def find(n):

            p1 = parent[n]

            while p1 != parent[p1]:
                parent[p1] = parent[parent[p1]]
                p1 = parent[p1]
            
            return p1
        
        def union(n1,n2):
            nonlocal groups
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if size[p1] > size[p2]:
                size[p1] += size[p2]
                parent[p2] = p1
            else:
                size[p2] += size[p1]
                parent[p1] = p2
            groups -= 1
            return True
        

        for n1,n2 in edges:
            union(n1,n2)
        return groups



