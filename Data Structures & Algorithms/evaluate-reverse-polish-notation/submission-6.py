class Solution:
    def calculate(self, a, b, operand):
        if operand == '+':
            return a+b
        elif operand == '-':
            return a-b
        elif operand == '*':
            return a*b
        else:
            return int(a/b)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "-*+/":
                b = stack.pop()
                a = stack.pop()
                stack.append(self.calculate(a,b,token))
            else:
                stack.append(int(token))
        return stack[-1]