class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        res = 0
        resAns = []
        for c in nums:
            hashMap[c] = hashMap.get(c,0) + 1
        
        for c in nums:
            hashMap[c] = hashMap.get(c,0) - 1
            if target - c in hashMap and hashMap[target - c] > 0:
                res = c
            hashMap[c] = hashMap.get(c,0) + 1
        
        for index, c in enumerate(nums):
            if c == res:
                resAns.append(index)
            elif c == target - res:
                if (not resAns) or index != resAns[0]:
                    resAns.append(index)
        
        resAns.sort()
        return resAns

        