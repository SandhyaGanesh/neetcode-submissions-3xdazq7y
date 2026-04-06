class TrieNode:
    def __init__(self, val='#', nex=None, isLeaf=False):
        self.val = val
        self.next = nex if nex else [None for _ in range(26)]
        self.isLeaf = isLeaf
        self.isAdded = False

class WordDict:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if not curr.next[ord(c)-ord('a')]:
                curr.next[ord(c)-ord('a')] = TrieNode(c)
            curr = curr.next[ord(c)-ord('a')]
        curr.isLeaf = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        wordDict = WordDict()
        for word in words:
            wordDict.insert(word)
        
        r = len(board)
        c = len(board[0])
        visited = [[False]*c for _ in range(r)]

        def helper(ix, iy, path, curr):
            if not curr:
                return
            
            if curr.isLeaf:
                if not curr.isAdded:
                    res.append(''.join(path))
                    curr.isAdded = True
            
            
            if ix + 1 < r and not visited[ix+1][iy]:
                nextCurr = curr.next[ord(board[ix+1][iy])-ord('a')]
                if nextCurr:
                    path.append(board[ix+1][iy])
                    visited[ix+1][iy] = True
                    helper(ix+1, iy, path, nextCurr)
                    visited[ix+1][iy] = False
                    path.pop()

            if ix - 1 >= 0 and not visited[ix-1][iy]:                
                nextCurr = curr.next[ord(board[ix-1][iy])-ord('a')]
                if nextCurr:
                    path.append(board[ix-1][iy])
                    visited[ix-1][iy] = True
                    helper(ix-1, iy, path, nextCurr)
                    visited[ix-1][iy] = False
                    path.pop()

            if iy + 1 < c and not visited[ix][iy+1]:
                nextCurr = curr.next[ord(board[ix][iy+1])-ord('a')]
                if nextCurr:
                    path.append(board[ix][iy+1])
                    visited[ix][iy+1] = True
                    helper(ix, iy+1, path, nextCurr)
                    visited[ix][iy+1] = False
                    path.pop()
                
            if iy - 1 >= 0 and not visited[ix][iy-1]:
                nextCurr = curr.next[ord(board[ix][iy-1])-ord('a')]
                if nextCurr:
                    path.append(board[ix][iy-1])
                    visited[ix][iy-1] = True
                    helper(ix, iy-1, path, nextCurr)
                    visited[ix][iy-1] = False
                    path.pop()
        
        for ix in range(r):
            for iy in range(c):
                visited[ix][iy] = True
                helper(ix,iy,[board[ix][iy]], wordDict.root.next[ord(board[ix][iy])-ord('a')])
                visited[ix][iy] = False
        
        return res