class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = (right - left) * min(heights[left], heights[right])

        while (right > left):
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1

            area = max(area, (right - left) * min(heights[left], heights[right]))

        return area
        