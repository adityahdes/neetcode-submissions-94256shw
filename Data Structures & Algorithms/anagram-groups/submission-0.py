class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        b = []
        for i in range(len(strs)):
            s = list(strs[i])
            s.sort()
            st = ''.join(s)
            if st in a:
                b[a[st]].append(strs[i])
            else:
                a[st] = len(a)
                b.append([strs[i]])
        return b
