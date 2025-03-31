class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_1= max(nums)
        nums.pop(nums.index(max_1))
        return((max_1-1)*(max(nums)-1))