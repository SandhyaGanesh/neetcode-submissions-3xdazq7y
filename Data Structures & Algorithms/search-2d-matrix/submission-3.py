class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        i = 0
        e = r
        while i < e:
            mid = (i+e)//2
            if matrix[mid][c - 1] > target:
                if matrix[mid][0] <= target:
                    break
                e = mid
            elif matrix[mid][0] < target:
                if matrix[mid][c - 1] >= target:
                    break
                i = mid + 1
            else:
                break
        
        print(i, e, mid)
        i = 0
        e = c
        while i < e:
            midc = (i+e)//2
            if matrix[mid][midc] > target:
                e = midc
            elif matrix[mid][midc] < target:
                i = midc + 1
            else:
                return True
        
        return False