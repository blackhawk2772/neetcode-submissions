class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])


        maximum = 0

        def dfs(x,y):
            
            if grid[x][y] == 0:
                return 0
            
            grid[x][y] = 0
            current = 1
            
            directions = [1,0], [-1,0], [0,1], [0,-1]
            for dr,dl in directions:
                posx = x + dr
                posy = y + dl
                if posx >= 0 and posx < m and posy >= 0 and posy < n and grid[posx][posy] == 1:
                    current +=dfs(posx,posy)

            return current

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maximum = max(maximum, dfs(i,j))
        return maximum