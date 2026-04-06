class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            curMin = self.stack[-1][1]
            self.stack.append((val,min(curMin, val)))

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()[0]

    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
