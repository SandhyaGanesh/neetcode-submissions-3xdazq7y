class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        path = set()
        isTrue = False

        def validNextSteps(x: int, y: int):
            nextSteps = []
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            for dx, dy in directions:
                if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]):
                    nextSteps.append((x+dx, y+dy))
            return nextSteps
        
        def recurse(x: int, y: int, s: str):
            nonlocal isTrue
            if s == word:
                isTrue = True
                return True
            
            for nx, ny in validNextSteps(x, y):
                if (nx, ny) not in path:
                    path.add((nx,ny))
                    if recurse(nx, ny, s+board[nx][ny]):
                        return True
                    path.remove((nx,ny))    

        for x in range(r):
            for y in range(c):
                path.add((x,y))
                if recurse(x, y, board[x][y]):
                    return True
                path.remove((x,y))

        return True if isTrue else False