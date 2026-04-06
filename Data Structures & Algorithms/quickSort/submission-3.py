# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def __init__(self):
        self.pairs = []

    def quickSortHelper(self, startIndex, pivotIndex):
        print(startIndex, pivotIndex)
        if startIndex >= pivotIndex:
            return
        insertIndex = startIndex
        traverseIndex = startIndex
        
        while traverseIndex < pivotIndex:
            if self.pairs[traverseIndex].key < self.pairs[pivotIndex].key:
                self.pairs[traverseIndex], self.pairs[insertIndex] = self.pairs[insertIndex], self.pairs[traverseIndex]
                insertIndex += 1
            traverseIndex += 1
        
        self.pairs[insertIndex], self.pairs[pivotIndex] = self.pairs[pivotIndex], self.pairs[insertIndex]
        self.quickSortHelper(startIndex, insertIndex - 1)
        self.quickSortHelper(insertIndex + 1, pivotIndex)


    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.pairs = pairs
        self.quickSortHelper(0, len(pairs) - 1)
        return self.pairs
        
        