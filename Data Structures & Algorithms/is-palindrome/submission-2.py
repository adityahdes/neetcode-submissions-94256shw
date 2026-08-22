class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = (''.join(filter(str.isalnum, s))).lower()
        if len(cleaned) <= 1:
            return True
        for i in range(len(cleaned)):
            if(len(cleaned) - i <= i):
                return True
            elif(cleaned[i] != cleaned[len(cleaned) - i - 1]):
                return False
            else:
                continue
        return False