class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        
        while i <= j:
            k = (i + j) // 2
            mid = nums[k]
            
            if mid == target:
                return k
            elif mid < target:
                i = k + 1
            else:
                j = k - 1
        
        return -1
