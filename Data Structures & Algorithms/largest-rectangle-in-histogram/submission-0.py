class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [-1]
        maxi = 0
        for i in range(len(heights)):
            while s[-1] != -1 and heights[s[-1]] >= heights[i]:
                h = heights[s.pop()]
                w = i - s[-1] - 1
                maxi = max(maxi, h * w)
            s.append(i)
        
        while s[-1] != -1:
            h = heights[s.pop()]
            w = len(heights) - s[-1] - 1
            maxi = max(maxi, h * w)
        return maxi

        