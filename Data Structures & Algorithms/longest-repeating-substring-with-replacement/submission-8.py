class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = len(s)
        windowMap = [0]*26
        windowMap[ord(s[0])-ord('A')] = 1
        result = 1

        i = 0
        e = 0

        while i <= e < l:
            maxf = max(windowMap)
            if e - i + 1 <= maxf + k:
                result = max(result, e - i + 1)
            # maxc = 'A'
            # for index in range(26):
            #     if windowMap[index] == maxf:
            #         maxc = chr(index+ord('A'))
            #         break
            print(i, e, result, maxf)
            if e - i + 1 > maxf + k:
                windowMap[ord(s[i])-ord('A')] -= 1
                i += 1
            else:
                e += 1
                if e < l:
                    windowMap[ord(s[e])-ord('A')] += 1
        
        return result