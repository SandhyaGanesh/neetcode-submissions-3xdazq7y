class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charMap = {}
        l = len(s)
        for i in range(l):
            charMap[s[i]] = i
        
        res = []
        start = 0
        end = 0
        i = 0
        while i < l:
            end = max(charMap[s[i]], end)
            if i == end:
                res.append(end + 1 - start)
                start = end + 1
            i += 1
        return res