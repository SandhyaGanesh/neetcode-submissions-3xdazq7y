class Solution:
    def getDigitSquare(self, n: int) -> int:
        res = 0
        while n:
            res += (n%10)*(n%10)
            n = n//10
        return res
    def isHappy(self, n: int) -> bool:
        n1 = n
        n2 = n
        while True:
            if self.getDigitSquare(n1) == 1:
                return True
            if self.getDigitSquare(n1) == self.getDigitSquare(self.getDigitSquare(n2)):
                return False
            n1 = self.getDigitSquare(n1)
            n2 = self.getDigitSquare(self.getDigitSquare(n2))