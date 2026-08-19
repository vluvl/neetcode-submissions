class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxW = -1
        while l < r:
            water = (r-l)*min(heights[r],heights[l])
            if water > maxW:
                maxW = water
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxW

