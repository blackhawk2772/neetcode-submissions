class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from heapq import heappop, heappush, heapify

        # [7, 5, 8]
        # [-7,-5,-8]
        stones = [-s for s in stones]
        # [-8,-7,-5]
        heapify(stones)

        while len(stones) > 1:
            
            if stones[0] == stones[1]:
                heappop(stones)
                heappop(stones)
            else:
                val1 = heappop(stones)
                val2 = heappop(stones)
                heappush(stones, val1-val2)
                
        if not stones:
            return 0
        else:
            return -(stones[0])