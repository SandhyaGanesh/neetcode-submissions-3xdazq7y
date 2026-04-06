class Solution:
    def maxNonZeroProduct(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        if l == 2:
            return max(max(nums), nums[0]*nums[1])
        
        r = 1
        for num in nums:
            r *= num
        if r > 0:
            return r

        leftSubarrayProduct = nums[0]
        rightSubarryProduct = r/(nums[0]*nums[1])
        res = max(leftSubarrayProduct, rightSubarryProduct)

        for i in range(1, l-1):
            leftSubarrayProduct *= nums[i]
            rightSubarryProduct /= nums[i+1]
            res = max(leftSubarrayProduct, rightSubarryProduct, res)
        
        return int(res)

    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        zeroIndices = [-1]
        for i in range(l):
            if nums[i] == 0:
               zeroIndices.append(i)
        zeroIndices.append(i+1)

        res = nums[0]
        for i in range(len(zeroIndices)-1):
            newNums = nums[zeroIndices[i]+1:zeroIndices[i+1]]
            if newNums:
                res = max(res, self.maxNonZeroProduct(newNums))
        
        if len(zeroIndices) > 2:
            return max(res, 0)
        else:
            return res
         
