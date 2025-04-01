class Solution:
    def maxArea(self, height: List[int]) -> int:
        left: int = 0
        right: int = len(height) - 1
        max: int = 0

        while(left < right):
            area: int = min(height[left],height[right])*(right-left)
            if area > max:
                max= area
            if height[right] > height[left]:
                left+= 1
            else:
                right-= 1
        
        return max