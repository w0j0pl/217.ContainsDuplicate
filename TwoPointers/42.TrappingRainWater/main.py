class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        center_left = left + 1
        right = len(height) - 1
        center_right = right - 1
        water = 0

        while left < right:

            if height[left] > height[right]:

                while height[right] > height[center_right]:

                    water += height[right] - height[center_right]
                    center_right -= 1

                right = center_right
                center_right = right - 1
                
            else:

                while height[left] > height[center_left]:

                    water += height[left] - height[center_left]
                    center_left += 1

                left = center_left
                center_left = left + 1
                
        return water