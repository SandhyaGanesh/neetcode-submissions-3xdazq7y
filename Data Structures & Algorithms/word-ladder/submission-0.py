class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        l = len(wordList)
        wordSet = set(wordList)
        def getNeighbors(word):
            res = []
            for index in range(len(word)):
                for i in range(ord('a'), ord('z')+1):
                    if word[index] == chr(i):
                        continue
                    newWord = word[:index]+chr(i)+word[index+1:]
                    if newWord in wordSet:
                        res.append(newWord)
                        wordSet.remove(newWord)
            return res
        
        q = deque()
        q.append(beginWord)
        jumps = 0
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word in wordSet:
                    wordSet.remove(word)
                if word == endWord:
                    return jumps+1
                for neighbor in getNeighbors(word):
                    q.append(neighbor)
            jumps += 1
        return 0

