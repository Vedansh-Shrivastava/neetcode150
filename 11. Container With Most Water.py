class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) -1
        area = 0 

        while left < right:
            num = (right - left) * min(height[left], height[right])
            area = max(area, num)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return area


            