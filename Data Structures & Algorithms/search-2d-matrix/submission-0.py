class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m
        foundrow = -1

        while l < r:
            mid = (l+r)//2
            if matrix[mid][0] <= target <= matrix[mid][n-1]:
                foundrow = mid
                break
            elif matrix[mid][0] > target:
                r = mid
            elif matrix[mid][n-1] < target:
                l = mid + 1
        
        if foundrow == -1:
            return False
        
        l = 0
        r = n

        while l < r:
            mid = (l+r)//2
            if matrix[foundrow][mid] == target:
                return True
            elif matrix[foundrow][mid] > target:
                r = mid
            elif matrix[foundrow][mid] < target:
                l = mid + 1
        
        return False