class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        startPtr = 0
        endPtr = l - 1
        while startPtr < endPtr:
            currSum = numbers[startPtr] + numbers[endPtr]
            if currSum < target:
                startPtr += 1
            elif currSum > target:
                endPtr -= 1
            else:
                return [startPtr + 1 , endPtr + 1]
        return [0,0]
        