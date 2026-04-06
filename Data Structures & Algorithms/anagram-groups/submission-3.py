class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqBuckets = {}
        for s in strs:
            bucket = [0]*26
            for c in s:
                bucket[ord(c)-ord('a')] += 1
            tmp = freqBuckets.get(tuple(bucket), [])
            tmp.append(s)
            freqBuckets[tuple(bucket)] = tmp
        return list(freqBuckets.values())