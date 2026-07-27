class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)

        i = 0
        e = l - 1

        while i < e:
            currSum = numbers[i] + numbers[e]
            if currSum > target:
                e -= 1
            elif currSum < target:
                i += 1
            else:
                return [i + 1, e + 1]
        
        return []