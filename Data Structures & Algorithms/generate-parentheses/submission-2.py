class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recurse(numOpen, n, runningStr):
            if len(runningStr) == 2*n and numOpen == 0:
                res.append(runningStr)
                return
            if len(runningStr) > 2*n:
                return
            if numOpen > 0:
                recurse(numOpen - 1, n, runningStr + ')')
            if n - numOpen > 0:
                recurse(numOpen + 1, n, runningStr + '(')
        
        recurse(0, n, '')
        return res
