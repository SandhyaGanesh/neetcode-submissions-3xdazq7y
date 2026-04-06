class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + ","
            for c in s:
                res += str(ord(c)) + ","
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        l = s.split(",")
        l = l[0:-1]
        r = []
        i = 0
        while i < len(l):
            r.append(l[i+1:i+int(l[i])+1])
            i += int(l[i])+1
        ans = []
        for rr in r:
            res = ""
            for c in rr:
                res += chr(int(c))
            ans.append(res)
        return ans
