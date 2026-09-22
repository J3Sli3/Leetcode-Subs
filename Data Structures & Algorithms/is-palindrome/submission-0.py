class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(filter(str.isalnum, s)).lower()
        s2 = ''.join(filter(str.isalnum, reversed(s))).lower()
        return s1 == s2


