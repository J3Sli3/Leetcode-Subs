class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        s = sorted(nums)
        l = []
        count = 0
        for i in range(1, len(s)):
            if count == 0:
                count += 1
            if s[i] == s[i-1] + 1:
                count += 1
            elif s[i] == s[i-1]:
                continue
            else:
                l.append(count)
                count = 0
        l.append(count)
        print(l)
        return max(l)

                
