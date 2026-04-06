class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = len(numbers)
        s = 0
        e = l - 1
        while s < e:
            curSum = numbers[s] + numbers[e]
            if curSum > target:
                e -= 1
            elif curSum < target:
                s += 1
            else:
                return [s+1, e+1]