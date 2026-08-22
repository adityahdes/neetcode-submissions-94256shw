class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest = 0
        i = 0
        j = len(heights) - 1
        while(j > i):
            hi = heights[i]
            hj = heights[j]
            h = min(hi, hj)
            a = (j - i) * h
            if a > biggest:
                biggest = a
            if hj > hi:
                i += 1
            else:
                j -= 1
        return biggest