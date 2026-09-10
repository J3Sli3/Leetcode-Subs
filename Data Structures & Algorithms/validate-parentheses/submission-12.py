class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        c = {']':'[', '}':'{', ')': '('}
        b = {'(','{','['}
        for i in range(len(s)):
            if s[i] in b:
                l.append(s[i])
            elif len(l) > 0:
                if c[s[i]] != l[-1]:
                    return False
                l.pop()
            else:
                return False
        if l:
            return False
        else:
            return True
