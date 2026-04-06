class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0]*9
        col = [0]*9
        box = [0]*9

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                num = int(board[r][c])
                
                if 1 << num & row[r]:
                    return False
                if 1 << num & col[c]:
                    return False
                if 1 << num & box[(r//3)*3 + (c//3)]:
                    return False
                
                row[r] |= 1 << num
                col[c] |= 1 << num
                box[(r//3)*3 + (c//3)] |= 1 << num
        return True