class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        directions = [1,0],[-1,0],[0,1],[0,-1],

        def dfs(x,y):

            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == "0":
                return
            
            grid[x][y] = "0"

            for dl,dr in directions:
                posx = x + dl
                posy = y + dr
                dfs(posx, posy)
            
        n_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    n_islands += 1
        
        return n_islands
        


