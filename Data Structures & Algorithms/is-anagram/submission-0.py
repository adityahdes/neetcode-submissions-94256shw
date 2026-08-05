class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = list(s)
        sorted_t = list(t)
        sorted_s.sort()
        sorted_t.sort()
        return sorted_s == sorted_t