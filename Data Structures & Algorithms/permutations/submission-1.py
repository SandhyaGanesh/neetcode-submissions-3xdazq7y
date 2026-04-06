class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        res = []
        numSet = set(nums)

        def helper(numSet, curr):
            print(numSet, curr)
            if len(curr) == l:
                res.append(curr.copy())
                return
            
            for num in numSet:
                curr.append(num)
                numSet.remove(num)
                
                helper(numSet.copy(), curr)
                numSet.add(num)
                curr.pop()
        
        helper(numSet.copy(), [])
        return res