class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        for s in strs:
            freqArr = [0]*26
            for c in s:
                freqArr[ord(c)-ord('a')] += 1
            bucket = buckets.get(tuple(freqArr), [])
            bucket.append(s)
            buckets[tuple(freqArr)] = bucket
        res = []
        for bucket, s in buckets.items():
            res.append(s)
        return res