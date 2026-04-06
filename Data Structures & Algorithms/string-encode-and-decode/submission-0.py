class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        l = str(len(strs))
        res += l + ':'
        for s in strs:
            res += str(len(s))+':'
        res += ''.join(strs)
        print("Encode", res)
        return res

    def decode(self, s: str) -> List[str]:
        n = int(s.split(':')[0])
        l = s.split(':')[1:n+1]
        news = ':'.join(s.split(':')[n+1:])
        ptr = 0
        res = []
        for i in range(n):
            
            sl = int(l[i])
            print(ptr,sl,i,news[ptr: ptr+sl])

            res.append(news[ptr: ptr+sl])
            ptr = ptr + sl
        print("Decode", res)
        return res