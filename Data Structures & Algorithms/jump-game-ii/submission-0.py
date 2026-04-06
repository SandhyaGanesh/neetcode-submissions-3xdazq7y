class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        minJumps = [9999]*l
        minJumps[l-1] = 0

        for i in range(l-2, -1, -1):
            if nums[i]+i >= l-1:
                minJumps[i] = 1
            else:
                for j in range(1, nums[i]+1):
                    minJumps[i] = min(minJumps[i+j]+1, minJumps[i])
        return minJumps[0]
