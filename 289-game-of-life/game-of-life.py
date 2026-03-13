class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])
        copy = [row[:] for row in board]

        for r in range(rows):
            for c in range(cols):
                up        = copy[r-1][c]   if r-1 >= 0 else 0
                down      = copy[r+1][c]   if r+1 < rows else 0
                left      = copy[r][c-1]   if c-1 >= 0 else 0
                right     = copy[r][c+1]   if c+1 < cols else 0
                top_left  = copy[r-1][c-1] if r-1 >= 0 and c-1 >= 0 else 0
                top_right = copy[r-1][c+1] if r-1 >= 0 and c+1 < cols else 0
                bot_left  = copy[r+1][c-1] if r+1 < rows and c-1 >= 0 else 0
                bot_right = copy[r+1][c+1] if r+1 < rows and c+1 < cols else 0

                neighbors = up + down + left + right + top_left + top_right + bot_left + bot_right

                if copy[r][c] == 1:
                    board[r][c] = 1 if neighbors in [2, 3] else 0
                else:
                    board[r][c] = 1 if neighbors == 3 else 0

        



        