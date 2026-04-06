class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(op, cl, curr):
            print(op, cl, curr)
            if op == cl == n:
                res.append(''.join(curr[:]))
                return
            if cl < op:
                curr.append(")")
                helper(op, cl + 1, curr)
                curr.pop()
            if op < n:
                curr.append("(")
                helper(op + 1, cl, curr)
                curr.pop()

        helper(0, 0, [])
        return res