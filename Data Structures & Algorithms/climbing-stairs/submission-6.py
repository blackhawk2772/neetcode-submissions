class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = [-1] * (n+1)

        def solver(n):
            
            if n == 0:
                return 1
            
            if n < 0:
                return 0

            if cache[n] == -1:
                cache[n] = solver(n-1) + solver(n-2)

            return cache[n]
            
        return solver(n)