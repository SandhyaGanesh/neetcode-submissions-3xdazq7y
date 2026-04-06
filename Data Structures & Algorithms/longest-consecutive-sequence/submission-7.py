class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        numMap = {}
        for num in nums:
            if num in numMap:
                continue
            if num + 1 in numMap and num - 1 in numMap:
                numMap[num] = (numMap[num+1][0] +1, numMap[num-1][1])
                start = numMap[num-1][1]
                numMap[start] = (numMap[start][0]+numMap[num][0], start)
                numMap[num+1] = (numMap[num+1][0], start)
            elif num + 1 in numMap:
                numMap[num] = (numMap[num+1][0] +1, num)
                numMap[num+1] = (numMap[num+1][0], numMap[num][1])
            elif num - 1 in numMap:
                numMap[num-1] = (numMap[num-1][0] +1, numMap[num-1][1])
                numMap[num] = (1, numMap[num-1][1])
                if num - 1 != numMap[num-1][1]:
                    numMap[numMap[num-1][1]] = (numMap[numMap[num-1][1]][0]+1, numMap[numMap[num-1][1]][1])
            else:
                numMap[num] = (1, num)
            print(numMap)
        res = []
        for v in numMap.values():
            res.append(v[0])
        return max(res)
        