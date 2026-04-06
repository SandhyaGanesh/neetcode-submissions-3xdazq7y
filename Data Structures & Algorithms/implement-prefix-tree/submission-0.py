class TrieNode:
    def __init__(self, val="#"):
        self.val = val
        self.next = [None for _ in range(26)]
        self.isLeaf = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()    

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not curr.next[ord(c)-ord('a')]:
                curr.next[ord(c)-ord('a')] = TrieNode(c)
            curr = curr.next[ord(c)-ord('a')]
        curr.isLeaf = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if not curr.next[ord(c)-ord('a')]:
                return False
            curr = curr.next[ord(c)-ord('a')]
        return curr.isLeaf

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if not curr.next[ord(c)-ord('a')]:
                return False
            curr = curr.next[ord(c)-ord('a')]
        return True
        
        