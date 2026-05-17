class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        

        visited = set()
        visiting = set()
        topSort = []
        adj = defaultdict(list)

        # we've made our adjacency list and now we are ready to dfs into it
        for s,d in edges:
            adj[s].append(d)

        def dfs(node):

            # if we are already visiting this node it means there is a graph
            if node in visiting:
                return False
            
            # if we've already visited this graph we skip it
            if node in visited:
                return True

            # mark that we are visiting this node
            visiting.add(node)

            for d in adj[node]:
                if not dfs(d):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            topSort.append(node)

            return True


        for i in range(n):
            if not dfs(i):
                return []

        topSort.reverse()
        return topSort
