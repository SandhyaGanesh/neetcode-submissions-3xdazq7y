class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freqMap = {}
        for i, num in enumerate(nums):
            print(i, num)
            f = freqMap.get(target-num, -1)
            print(f)
            if f != -1:
                print(min(f,i), max(f,i))
                return [min(f,i), max(f,i)]
            freqMap[num] = i
        return []