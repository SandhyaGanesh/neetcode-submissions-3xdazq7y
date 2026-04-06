class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tripletSet = set([tuple(triplet) for triplet in triplets])
        for i in range(3):
            for triplet in tripletSet.copy():
                if triplet[i] > target[i]:
                    tripletSet.remove(triplet)
        
        for i in range(3):
            found = False
            for triplet in tripletSet:
                if triplet[i] == target[i]:
                    found = True
            if not found:
                return False
        
        return True