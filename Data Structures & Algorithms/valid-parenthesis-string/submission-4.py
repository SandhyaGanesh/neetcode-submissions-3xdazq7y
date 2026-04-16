class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpenParan = 0
        maxOpenParan = 0
        for p in s:
            if p == '(':
                minOpenParan += 1
                maxOpenParan += 1
            elif p == ')':
                minOpenParan -= 1
                maxOpenParan -= 1
            else:
                minOpenParan -= 1
                maxOpenParan += 1
            if maxOpenParan < 0:
                return False
            if minOpenParan < 0:
                minOpenParan = 0
        return minOpenParan == 0