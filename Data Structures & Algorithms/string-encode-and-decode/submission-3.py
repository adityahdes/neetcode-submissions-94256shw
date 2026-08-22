class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            l = len(s)
            out = out + str(l) + "#" + s
        return(out)


    def decode(self, s: str) -> List[str]:
        out = []
        n = 0
        while n < len(s):
            temp = s[n:]
            j = temp.index('#')
            k = int(temp[0:j])
            x = s[n+j+1:n+j+1+k]
            out.append(x)
            n = n + j + k + 1
        return out
