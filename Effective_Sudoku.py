class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in board:
            tmp = []
            for j in i:
                if j == '.':
                    continue
                else:
                    if j in tmp:
                        return False
                    else:
                        tmp.append(j)

        for i in range(9):
            tmp = []
            for j in range(9):
                if board[j][i] == '.':
                    continue
                else:
                    if board[j][i] in tmp:
                        return False
                    else:
                        tmp.append(board[j][i])

        for i in range(9):
            tmp = []
            for j in range(9):
                x = int(i / 3)*3 + int(j / 3)
                y = i % 3 * 3 +j % 3
                if board[x][y] == '.':
                    continue
                else:
                    if board[x][y] in tmp:
                        return False
                    else:
                        tmp.append(board[x][y])
        return True

board1 = [
          ["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]
board2 = [
          ["8","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]
print(Solution().isValidSudoku(board1))
