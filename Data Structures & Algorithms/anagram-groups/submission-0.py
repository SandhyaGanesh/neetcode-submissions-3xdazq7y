class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        for word in strs:
            freq = [0]*26
            for c in word:
                freq[ord(c)-ord('a')] += 1
            freq = tuple(freq)
            get = buckets.get(freq, [])
            print(get)
            get.append(word)
            buckets[freq] = get
        
        res = []
        for key, value in buckets.items():
            res.append(value)
        return res
        