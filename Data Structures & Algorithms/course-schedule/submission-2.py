class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = set()
        visiting = set()
        topSort = []
        adj = defaultdict(list)

        for s, d in prerequisites:
            adj[s].append(d)

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            
            visiting.add(node)

            for d in adj[node]:
                if not dfs(d):
                    return False
                
            visiting.remove(node)
            visited.add(node)
            topSort.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

