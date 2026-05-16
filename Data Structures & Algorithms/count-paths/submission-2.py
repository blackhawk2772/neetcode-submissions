class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = {}

        def dfs(x,y):

            if x == m-1 and y == n-1:
                return 1

            if x< 0 or x>= m or y < 0 or y >= n:
                return 0
            
            if (x,y) in dp:
                return dp[(x, y)]

            dp[(x, y)] = dfs(x+1,y) + dfs(x,y+1)
            
            return dp[(x,y)]

        return dfs(0,0)