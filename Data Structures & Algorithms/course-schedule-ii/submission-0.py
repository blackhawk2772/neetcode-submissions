class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for src, dst in prerequisites:
            adj[src].append(dst)

        visited = set()
        visiting = set()
        topoSort = []

        def dfs(src):

            if src in visited:
                return True
            if src in visiting:
                return False
            
            visiting.add(src)

            for dst in adj[src]:
                if not dfs(dst):
                    return False
            
            visiting.remove(src)
            visited.add(src)
            topoSort.append(src)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return topoSort