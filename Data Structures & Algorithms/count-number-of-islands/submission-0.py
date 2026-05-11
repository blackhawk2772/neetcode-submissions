class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        def islandFinder(r,c):

            if grid[r][c] == "1":
                grid[r][c] = "0"
            else:
                return

            directions = [1, 0], [-1, 0],[0, -1], [0, 1]

            for dr,dc in directions:
                if r+dr >= 0 and r+dr < m and c+dc >= 0 and c + dc < n:
                    islandFinder(r+dr,c+dc)


        for i in range(m):
            for j in range(n):

                if grid[i][j] == "1":
                    islandFinder(i,j)
                    res += 1
        
        return res