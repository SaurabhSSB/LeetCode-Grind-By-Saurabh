class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k: int = len(nums)
        while val in nums:
            k-= 1
            nums.pop(nums.index(val))
        
        return(k)