class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)

        for s,d,w in times:
            adj[s].append([d,w])
        
        minHeap = [[0, k]]

        shortest = {}

        while minHeap:

            w1,n1 = heapq.heappop(minHeap)

            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2,w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2,n2])
        
        for i in range(1, n+1):
            if i not in shortest:
                return -1
                
        return max(shortest.values())
