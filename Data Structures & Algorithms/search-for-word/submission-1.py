class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(m: int, n: int, wp: int):

            if wp == len(word):
                return True

            if (
                 m < 0
                or m >= len(board)
                or n < 0
                or n >= len(board[0])
                or board[m][n] != word[wp]
                or board[m][n] == "#"
            ):
                return False

            board[m][n] = "#"

            if helper(m + 1, n, wp + 1):
                return True

            if helper(m - 1, n, wp + 1):
                return True

            if helper(m, n + 1, wp + 1):
                return True

            if helper(m, n - 1, wp + 1):
                return True

            board[m][n] = word[wp]
            return False

        for m in range(len(board)):
            for n in range(len(board[0])):
                if helper(m, n, 0):
                    return True
                    
        return False
