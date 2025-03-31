class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p: int = 1 
        s: int = 1
        size: int = len(nums)
        nums_2: list = []

        for i in range(size):
            nums_2.append(p)
            p*= nums[i]
        
        for j in range(size-1,-1,-1):
            nums_2[j]*= s
            s*= nums[j]
        
        return(nums_2)