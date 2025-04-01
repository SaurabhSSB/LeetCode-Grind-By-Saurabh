class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        x: int = max(nums)
        y: int = nums.index(x)
        nums.pop(y)
        
        for i in nums:
            if 2*i > x:
                return(-1)
        
        return(y)