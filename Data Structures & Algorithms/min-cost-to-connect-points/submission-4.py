class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([j, dist])
                adj[j].append([i, dist]) 
        
        

        minHeap = [[0,0]]
        shortest = {}

        while minHeap:
            w1,n1 = heapq.heappop(minHeap)

            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2,w2 in adj[n1]:

                if n2 not in shortest:
                    heapq.heappush(minHeap, [w2,n2])

        return sum(shortest.values())            
