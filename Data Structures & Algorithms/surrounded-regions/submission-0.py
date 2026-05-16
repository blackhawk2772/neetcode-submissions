class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        if not board or not board[0]:
            return

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        M = len(board)
        N = len(board[0])

        def dfs(x, y):
            if x < 0 or x >= M or y < 0 or y >= N:
                return

            if board[x][y] != "O":
                return

            board[x][y] = "#"

            for dx, dy in directions:
                dfs(x + dx, y + dy)

        # Mark all border-connected "O"s as safe
        for i in range(M):
            dfs(i, 0)
            dfs(i, N - 1)

        for j in range(N):
            dfs(0, j)
            dfs(M - 1, j)

        # Flip surrounded O -> X, and restore safe # -> O
        for i in range(M):
            for j in range(N):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"