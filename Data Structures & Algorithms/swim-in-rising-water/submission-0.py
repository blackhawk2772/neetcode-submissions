class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)

        minHeap = [[grid[0][0], [0,0]]]

        shortest = {}

        while minHeap:

            w1,n1 = heapq.heappop(minHeap)

            if (n1[0],n1[1]) in shortest:
                continue
            shortest[(n1[0], n1[1])] = w1

            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            current_row = n1[0]
            current_col = n1[1]
            for dr, dc in directions:
                new_row = current_row + dr
                new_col = current_col + dc
               
                if 0 <= new_row < n and 0 <= new_col < n:
                    if (new_row,new_col) not in shortest:
                        heapq.heappush(minHeap, [max(w1, grid[new_row][new_col]), [new_row,new_col]])
            
        return shortest[(n-1,n-1)]