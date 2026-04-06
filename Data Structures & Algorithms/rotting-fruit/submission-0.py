class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()
        numGoodBananas = 0
        minsPassed = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    numGoodBananas += 1
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))
        
        while q:
            if not numGoodBananas:
                return minsPassed
            for _ in range(len(q)):
                br, bc = q.popleft()
                if 0 <= br - 1 and grid[br-1][bc] == 1 and (br-1,bc) not in visited:
                    numGoodBananas -= 1
                    q.append((br-1,bc))
                    visited.add((br-1,bc))
                if 0 <= bc - 1 and grid[br][bc-1] == 1 and (br,bc-1) not in visited:
                    numGoodBananas -= 1
                    q.append((br,bc-1))
                    visited.add((br,bc-1))
                if br + 1 < rows and grid[br+1][bc] == 1 and (br+1,bc) not in visited:
                    numGoodBananas -= 1
                    q.append((br+1,bc))
                    visited.add((br+1,bc))
                if bc + 1 < cols and grid[br][bc+1] == 1 and (br,bc+1) not in visited:
                    numGoodBananas -= 1
                    q.append((br,bc+1))
                    visited.add((br,bc+1))
            minsPassed += 1
        
        if not numGoodBananas:
            return minsPassed
        else:
            return -1

                