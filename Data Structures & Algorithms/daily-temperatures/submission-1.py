class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        s = []
        for i,t in enumerate(temperatures):
            while s and t > s[-1][0]:
                temp,index = s.pop()
                res[index] = i - index
            s.append((t, i))
        return res