class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        l3 = l1 + l2
        num3 = ['0'] * l3
        carry = 0

        for j in range(l2 - 1, -1, -1):
            for i in range(l1 - 1, -1, -1):
                c1 = num1[i]
                c2 = num2[j]
                result = int(c1) * int(c2) + carry
                newResult = int(num3[i+j+1]) + result%10
                num3[i+j+1] = str(newResult%10)
                carry = result//10 + newResult//10
            newResult = int(num3[j]) + carry
            num3[j] = str(newResult%10)
            carry = newResult//10
        num3[0] = str(int(num3[0]) + carry)
        while num3 and num3[0] == '0':
            num3 = num3[1:]
        return ''.join(num3) if num3 else "0"