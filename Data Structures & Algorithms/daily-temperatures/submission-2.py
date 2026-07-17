class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        currMax = temperatures[0]
        tempStack = [(currMax, 0)]
        res = [0]*l
        i = 1
        while i < l:
            t = temperatures[i]
            while tempStack and t > tempStack[-1][0]:
                res[tempStack[-1][1]] = i - tempStack[-1][1]
                tempStack.pop()
            tempStack.append((t, i))
            i += 1
        return res                      


        