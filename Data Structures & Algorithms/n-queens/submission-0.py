class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        markedRow = [False for _ in range(n)]
        markedCol = [False for _ in range(n)]
        markedLD = [False for _ in range(2*n - 1)]
        markedRD = [False for _ in range(2*n - 1)]

        res = []

        def setMarking(ix, iy, mark):
            nonlocal markedRow, markedCol, markedLD, markedRD
            markedRow[ix] = mark
            markedCol[iy] = mark
            markedLD[ix + iy] = mark
            markedRD[ix - iy + n - 1] = mark
        
        def isMarked(ix, iy):
            nonlocal markedRow, markedCol, markedLD, markedRD
            if markedRow[ix] or markedCol[iy] or markedLD[ix + iy] or markedRD[ix - iy + n - 1]:
                return True
            return False

        def helper(ix, iy, path):
            if len(path) == n:
                res.append(path[:])
                return
            if ix + 1 < n:
                for y in range(n):
                    if not isMarked(ix + 1, y):
                        path.append("."*y+"Q"+"."*(n-y-1))
                        setMarking(ix + 1, y, True)
                        helper(ix + 1, y, path)
                        setMarking(ix + 1, y, False)
                        path.pop()


        for i in range(n):
            setMarking(0, i, True)
            helper(0, i, ["."*i+"Q"+"."*(n-i-1)])
            setMarking(0, i, False)
        
        return res