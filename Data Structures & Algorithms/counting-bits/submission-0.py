class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for number in range(n+1):
            numOnes = 0
            while number:
                if 1 & number == 1:
                    numOnes += 1
                number = number >> 1
            res.append(numOnes)
        return res
            