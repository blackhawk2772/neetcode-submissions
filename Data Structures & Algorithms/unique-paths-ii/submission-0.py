class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        path = {}

        def dfs(x, y):

            if x < 0 or x >= m or y < 0 or y >= n or obstacleGrid[x][y] == 1:
                return 0

            if x == m - 1 and y == n - 1:
                return 1

            if (x, y) not in path:
                path[(x, y)] = dfs(x + 1, y) + dfs(x, y + 1)

            return path[(x, y)]

        return dfs(0, 0)