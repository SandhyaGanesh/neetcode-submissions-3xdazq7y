class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {'}':'{', ']':'[', ')':'('}
        stack = []
        for b in s:
            if b in '{[(':
                stack.append(b)
            else:
                if not stack or stack.pop() != bracketMap[b]:
                    return False
        
        return True if not stack else False
