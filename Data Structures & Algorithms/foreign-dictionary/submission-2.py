class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {}
        inDegree = {}
        letterSet = set()
        wordOrder = []
        visited = set()

        for word in words:
            letters = list(word)
            for letter in letters:
                letterSet.add(letter)
        
        for letter in letterSet:
            adjList[letter] = []
            inDegree[letter] = 0
        
        l = len(words)
        for index in range(l-1):
            sWord = words[index]
            bWord = words[index + 1]
            hasCommonPrefix = True
            for i in range(min(len(sWord), len(bWord))):
                if sWord[i] != bWord[i]:
                    hasCommonPrefix = False
                    adjList[sWord[i]].append(bWord[i])
                    inDegree[bWord[i]] += 1
                    break
            if hasCommonPrefix and len(bWord) < len(sWord):
                return ""
            
        print(adjList)

        q = deque()
        for letter in letterSet:
            if inDegree[letter] == 0:
                q.append(letter)
                visited.add(letter)
        
        while q:
            letter = q.popleft()
            wordOrder.append(letter)
            for neighbor in adjList[letter]:
                if neighbor in visited:
                    return ""
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    q.append(neighbor)
                    visited.add(neighbor)
        
        return ''.join(wordOrder) if len(wordOrder) == len(letterSet) else ""

        

        