class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        heap = []
        for i in range(r):
            for j in range(c):
                heap.append((-1*matrix[i][j], (i,j)))
        heapq.heapify(heap)

        memo = {}
        maxRes = 1

        while heap:
            element, (i, j) = heapq.heappop(heap)
            memo[(i,j)] = memo.get((i,j), 1)
            neighbors = [(0,1), (1,0), (-1,0), (0,-1)]
            #print("Element, i, j, memo[(i,j)]:", matrix[i][j], i, j, memo[(i,j)])
            for di, dj in neighbors:
                if 0 <= i+di < r and 0 <= j+dj < c:
                    if matrix[i+di][j+dj] < matrix[i][j]:
                        
                        memo[(i+di,j+dj)] = max(memo.get((i+di,j+dj), 1), memo[(i,j)]+1)
                        #print("Neighbor, i, j, memo[(i+di,j+dj)]:", matrix[i+di][j+dj], i+di, j+dj, memo[(i+di,j+dj)])
                        maxRes = max(maxRes, memo[(i+di,j+dj)])
        return maxRes
        
