class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)

        for a,b in prerequisites:
            adj[a].append(b)

        visited = set()
        visiting = set()

        def dfs(src):

            if src in visited:
                return True # Already added
            if src in visiting:
                return False # Cycle detected

            visiting.add(src)

            for dst in adj[src]:
                if not dfs(dst):
                    return False
            
            visiting.remove(src)
            visited.add(src)

            return True

        for i in range(numCourses):
                if not dfs(i):
                    return False

        return True