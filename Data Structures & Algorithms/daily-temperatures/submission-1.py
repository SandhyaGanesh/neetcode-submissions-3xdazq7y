class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                temp = stack.pop()
                res[temp[1]] = i - temp[1]
            stack.append((temperatures[i], i))
        finalRes = [0 if i == -1 else i for i in res]
        return finalRes