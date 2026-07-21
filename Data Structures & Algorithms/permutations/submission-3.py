class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def generatePermutations(i, runningPermutation, remainingNums):
            if i == len(nums):
                result.append(runningPermutation)
                return
            for num in remainingNums:
                rm = remainingNums.copy()
                rm.remove(num)
                generatePermutations(i + 1, runningPermutation +[num], rm)
        generatePermutations(0, [], set(nums))
        return result
            
