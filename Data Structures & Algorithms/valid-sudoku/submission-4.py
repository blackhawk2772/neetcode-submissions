class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashrow = defaultdict(set)
        hashcol = defaultdict(set)
        hashsq = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if (board[i][j] in hashrow[i] or board[i][j] in hashcol[j] or board[i][j] in hashsq[(i // 3, j // 3)]):
                    return False
                
                hashrow[i].add(board[i][j])
                hashcol[j].add(board[i][j])
                hashsq[(i // 3, j // 3)].add(board[i][j])

        return True            
                
