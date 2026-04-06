class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        i = 0
        e = len(matrix)
        row = -1
        col = len(matrix[0])

        while i < e:
            middle = (i+e) // 2
            if matrix[middle][0] <= target <= matrix[middle][col-1]:
                row = middle
                break
            elif matrix[middle][col-1] < target:
                i = middle + 1
            elif matrix[middle][0] > target:
                e = middle
        
        if row == -1:
            return False

        i = 0
        e = col

        while i < e:
            middle = (i+e) // 2
            #print(middle)
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] < target:
                i = middle + 1
            elif matrix[row][middle] > target:
                e = middle
        return False