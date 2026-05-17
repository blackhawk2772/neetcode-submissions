class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def search(x, y):
            if grid[x][y] == 0:
                return

            grid[x][y] = 0

            for dl, dr in directions:
                posx = x + dl
                posy = y + dr

                if (
                    posx >= 0
                    and posy >= 0
                    and posx < M
                    and posy < N
                    and grid[posx][posy] == 1
                ):
                    search(posx, posy)

            return

        for i in range(M):
            if grid[i][0] == 1:
                search(i, 0)

            if grid[i][N - 1] == 1:
                search(i, N - 1)

        for i in range(N):
            if grid[0][i] == 1:
                search(0, i)

            if grid[M - 1][i] == 1:
                search(M - 1, i)

        res = 0

        for i in range(M):
            for j in range(N):
                res += grid[i][j]

        return res
