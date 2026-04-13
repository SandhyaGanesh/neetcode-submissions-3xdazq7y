class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        digits.reverse()
        for digit in digits:
            newDigit = digit + carry
            if newDigit > 9:
                carry = 1
                newDigit = newDigit - 10
            else:
                carry = 0
            res.append(newDigit)
        if carry:
            res.append(carry)
        res.reverse()
        return res