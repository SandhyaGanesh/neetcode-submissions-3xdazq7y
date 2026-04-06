class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def generatePermutation(curr, availableIndices):
            if len(curr) == len(nums):
                res.append(curr[:])
            
            for index in availableIndices.copy():
                curr.append(nums[index])
                availableIndices.remove(index)
                generatePermutation(curr, availableIndices)
                availableIndices.add(index)
                curr.pop()
        
        availableIndices = set([i for i in range(len(nums))])
        generatePermutation([], availableIndices)
        return res