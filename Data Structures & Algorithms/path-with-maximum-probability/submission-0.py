class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = defaultdict(list)

        for i, (s, d) in enumerate(edges):
            w = succProb[i]
            adj[s].append([d, w])
            adj[d].append([s, w])
        
        shortest = {}

        maxHeap = [[1, start_node]]

        while maxHeap:
            w1,n1 = heapq.heappop_max(maxHeap)

            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2,w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush_max(maxHeap, [w1 * w2, n2])
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = 0
        
        return shortest[end_node]
