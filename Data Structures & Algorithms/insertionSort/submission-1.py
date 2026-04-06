# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        stateList = []
        n = len(pairs)
        for ptr in range(1, n):
            leftPtr = ptr - 1
            rightPtr = ptr
            stateList.append(pairs.copy())
            while leftPtr >= 0:
                if pairs[leftPtr].key > pairs[rightPtr].key:
                    pairs[leftPtr], pairs[rightPtr] = pairs[rightPtr], pairs[leftPtr]
                    leftPtr -= 1
                    rightPtr -= 1
                else:
                    break
        stateList.append(pairs.copy())
        return stateList