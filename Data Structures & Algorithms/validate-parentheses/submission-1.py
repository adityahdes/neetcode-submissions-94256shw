class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pres = ['(', '{', '[']
        posts = [')', '}', ']']
        for c in s:
            if c in pres:
                stack.append(c)
            elif c in posts:
                if(len(stack) == 0): return False
                d = stack[-1]
                if d in posts:
                    return False
                n = pres.index(d)
                if c == posts[n]:
                    stack.pop()
                    continue
                else:
                    return False
        return len(stack) == 0
                