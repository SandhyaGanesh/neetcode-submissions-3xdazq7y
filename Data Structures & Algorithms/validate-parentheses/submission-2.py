class Solution:
    def isValid(self, s: str) -> bool:
        paraMap = {'}':'{', ']':'[', ')':'('}
        q = deque()
        for c in s:
            if c in paraMap.values():
                q.append(c)
            else:
                if not q or q.pop() != paraMap[c]:
                    return False
        return True if not q else False