class Solution:
    def jump(self, nums: List[int]) -> int:

        l = len(nums)
        if l == 1:
            return 0
        jumpsSoFar = 0
        waveBegin = 0
        waveEnd = 1
        nextWaveEnd = 1

        while waveBegin < l:
            for i in range(waveBegin, waveEnd):
                nextWaveEnd = max(nextWaveEnd, nums[i] + i)
                if nextWaveEnd >= l-1:
                    return jumpsSoFar + 1
            jumpsSoFar += 1
            waveBegin = waveEnd
            waveEnd = nextWaveEnd + 1
        
        return jumpsSoFar