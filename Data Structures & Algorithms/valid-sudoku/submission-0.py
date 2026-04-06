class Solution:

    def validateNums(self, nums: List[str]) -> bool:
        numSet = set()
        for num in nums:
            if num != '.' and num in numSet:
                return False
            numSet.add(num)
        return True
    
    # def validateRow(self, row: List[str]) -> bool:
    # def validateCol(self, col: List[str]) -> bool:
    # def validateBox(self, box: List[List[str]]) -> bool:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxStarts = [(0,0),(3,0),(6,0),(0,3),(3,3),(6,3),(0,6),(3,6),(6,6)]
        for i in range(9):
            if not self.validateNums(board[i]):
                return False
            colNums = [board[c][i] for c in range(9)]
            if not self.validateNums(colNums):
                return False
            boxNums = []
            R,C = boxStarts[i]
            for r in range(3):
                for c in range(3):
                    boxNums.append(board[R+r][C+c])
            if not self.validateNums(boxNums):
                return False
        return True