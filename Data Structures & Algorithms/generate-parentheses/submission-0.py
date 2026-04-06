class Solution:
    def __init__(self):
        self.res = []

    def paranthesisHelper(self, o, c, seq):
        if o == 0 and c == 0:
            self.res.append(seq)
        
        if o > 0:
            self.paranthesisHelper(o - 1, c, seq + "(")
        if c > o:
            self.paranthesisHelper(o, c - 1, seq + ")")

    def generateParenthesis(self, n: int) -> List[str]:
        self.paranthesisHelper(n, n, "")
        return self.res
        