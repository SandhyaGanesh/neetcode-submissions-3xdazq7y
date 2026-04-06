class TrieNode:
    def __init__(self, val="#", nex=None, isLeaf=False):
        self.val = val
        self.next = nex if nex else [None for _ in range(26)]
        self.isLeaf = isLeaf

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not curr.next[ord(c)-ord('a')]:
                curr.next[ord(c)-ord('a')] = TrieNode(c)
            curr = curr.next[ord(c)-ord('a')]
        curr.isLeaf = True

    def search(self, word: str, curr=None) -> bool:
        if not curr:
            curr = self.root
        print(curr.val, word)
        for i in range(len(word)):
            c = word[i]
            if c == ".":
                for x in range(26):
                    currnext = TrieNode(curr.val, curr.next, curr.isLeaf)
                    if self.search(chr(x+ord('a'))+word[i+1:], currnext):
                        return True
                return False
            else:        
                if not curr.next[ord(c)-ord('a')]:
                    return False
                curr = curr.next[ord(c)-ord('a')]
        return curr.isLeaf
