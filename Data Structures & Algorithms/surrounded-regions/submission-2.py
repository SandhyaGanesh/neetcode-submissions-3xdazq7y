class Solution:
    def getNeighbors(self, ix, iy, r, c):
        directions = [(-1, 0), (1, 0), (0, -1), (0,1)]
        neighbors = []
        for dx, dy in directions:
            if 0 <= ix+dx < r and 0 <= iy+dy < c:
                neighbors.append((ix+dx, iy+dy))
        return neighbors
    
    def solve(self, board: List[List[str]]) -> None:
        r = len(board)
        c = len(board[0])
        for g in board:
            print(g)

        def markSafe(ix, iy):
            print(ix, iy)
            board[ix][iy] = 'S'
            neighbors = self.getNeighbors(ix, iy, r, c)
            for nx, ny in neighbors:
                if board[nx][ny] == 'O':
                    markSafe(nx, ny)
        
        print("After")
        for ix in range(r):
            for iy in [0, c-1]:
                if board[ix][iy] == 'O':
                    markSafe(ix, iy)
        for iy in range(c):
            for ix in [0, r-1]:
                if board[ix][iy] == 'O':
                    markSafe(ix, iy)
        for ix in range(r):
            for iy in range(c):
                if board[ix][iy] == 'O':
                    board[ix][iy] = 'X'
                if board[ix][iy] == 'S':
                    board[ix][iy] = 'O'
        for g in board:
            print(g)
        
        return