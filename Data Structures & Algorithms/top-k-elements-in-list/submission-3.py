class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = [0]*2001
        res = {}
        for num in nums:
            freqDict[num+1000] += 1
        for i in range(len(freqDict)):
            tmp = res.get(freqDict[i], [])
            tmp.append(i-1000)
            res[freqDict[i]] = tmp
        r = sorted(res.items(), reverse=True)
        r = r[0:-1]
        return [x for sublist in [i[1] for i in r[0:k]] for x in sublist][0:k]

        
