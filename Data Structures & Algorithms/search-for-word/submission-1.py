class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        r = len(board)
        c = len(board[0])
        visited = [[False]*c for i in range(r)]

        def helper(ix, iy, path):
            nonlocal res
            print(''.join(path))
            s = ''.join(path)
            if s == word:
                print("here")
                res = True
                return
            if len(path) >= len(word):
                return
            if ''.join(path[:len(path)]) != word[:len(path)]:
                return
            
            if 0 <= ix + 1 < r and not visited[ix+1][iy]:
                path.append(board[ix+1][iy])
                visited[ix+1][iy] = True
                helper(ix + 1, iy, path)
                visited[ix+1][iy] = False
                path.pop()
            if 0 <= ix - 1 < r and not visited[ix-1][iy]:
                path.append(board[ix-1][iy])
                visited[ix-1][iy] = True
                helper(ix - 1, iy, path)
                visited[ix-1][iy] = False
                path.pop()
            if 0 <= iy + 1 < c and not visited[ix][iy+1]:
                path.append(board[ix][iy+1])
                visited[ix][iy+1] = True
                helper(ix, iy+1, path)
                visited[ix][iy+1] = False
                path.pop()
            if 0 <= iy - 1 < c and not visited[ix][iy-1]:
                path.append(board[ix][iy-1])
                visited[ix][iy-1] = True
                helper(ix, iy-1, path)
                visited[ix][iy-1] = False
                path.pop()
        
        for ix in range(r):
            for iy in range(c):
                visited[ix][iy] = True
                helper(ix,iy, [board[ix][iy]])
                visited[ix][iy] = False
        return res
            


        