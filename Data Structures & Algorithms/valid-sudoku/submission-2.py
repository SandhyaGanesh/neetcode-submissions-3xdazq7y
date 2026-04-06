class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            numMap = {}
            for c in row:
                if c != "." and c in numMap:
                    return False
                numMap[c] = True
        for c in range(9):
            numMap = {}
            for r in range(9):
                if board[r][c] != "." and board[r][c] in numMap:
                    return False
                numMap[board[r][c]] = True
        for rm in range(3):
            for rc in range(3):
                numMap = {}
                for r in range(3):
                    for c in range(3):
                        element = board[3*rm+r][3*rc+c]
                        if element != "." and element in numMap:
                            return False
                        numMap[element] = True
        return True
        