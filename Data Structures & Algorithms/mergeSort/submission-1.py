# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
import math

class Solution:
    def __init__(self):
        self.pairs = []

    def mergeTwo(self, start, mid, end):
        leftPointer = start
        rightPointer = mid+1
        newArr = []
        while leftPointer <= mid or rightPointer <= end:
            leftVal = Pair(math.inf, "")
            rightVal = Pair(math.inf, "")
            if leftPointer <= mid:
                leftVal = self.pairs[leftPointer]
            if rightPointer <= end:
                rightVal = self.pairs[rightPointer]
            if leftVal.key <= rightVal.key:
                newArr.append(leftVal)
                leftPointer += 1
            else:
                newArr.append(rightVal)
                rightPointer += 1

        for i in range(start, end+1):
            self.pairs[i] = newArr[i - start]        
    
    def customMergeSort(self, start, end):
        if end == start:
            return
        
        mid = (start + end)//2
        self.customMergeSort(start, mid)
        self.customMergeSort(mid+1, end)
        self.mergeTwo(start, mid, end)

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.pairs = pairs
        end = len(pairs) - 1
        start = 0
        if end == -1:
            return []
        self.customMergeSort(start, end)
        return pairs