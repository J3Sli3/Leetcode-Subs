class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        c = {']':'[', '}':'{', ')': '('}
        b = {'(','{','['}
        for i in range(len(s)):
            if s[i] in b:
                l.append(s[i])
            elif (len(l) > 0): 
                if (c[s[i]] != l[len(l) - 1]):
                    return False
                else:
                    l.pop()
            else:
                return False
            print(len(l) - 1)
        if len(l) == 0:
            return True
        else:
            return False
