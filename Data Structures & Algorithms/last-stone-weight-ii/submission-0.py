class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        total = sum(stones)
        cache = {}

        def solver(i, val):

            if i == len(stones):
                return abs(total- 2*val)

            if (i, val) in cache:
                return cache[(i,val)]
            
            a = solver(i+1, val)
            b = solver(i+1, val+stones[i])
            
            cache[(i,val)] = min(a,b)

            return cache[(i,val)]

        return solver(0, 0)