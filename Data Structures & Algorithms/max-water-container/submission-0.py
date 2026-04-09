class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # distance * height (lower end)
        maxArea = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxArea = max(maxArea, area)

            # should l++ or r--?
            # move the lower end

            if (heights[l] <= heights[r]):
                l += 1
            else:
                r -= 1

        return maxArea