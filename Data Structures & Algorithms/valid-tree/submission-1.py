class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False

        size = [1] * n
        parent = [i for i in range(n)]

        def find(n):
            
            p1 = parent[n]
            
            while p1 != parent[p1]:
                parent[p1] = parent[parent[p1]]
                p1 = parent[p1]
            return p1
        
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if size[p1] > size[p2]:
                size[p1] += size[p2]
                parent[p2] = p1
            else:
                size[p2] += size[p1]
                parent[p1] = p2
            
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return False
        return True