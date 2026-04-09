class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # area = height (shorter end) * width (j-i)

        # brute force: O(n^2)

        l, r = 0, len(heights) - 1
        maxA = 0

        while l < r:
            curH = min(heights[l], heights[r])
            curW = r - l
            curA = curH * curW
            maxA = max(maxA, curA)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return maxA