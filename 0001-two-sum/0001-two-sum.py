class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num: list[int] = [target-i for i in nums]
        for i in range(len(num)):
            if num[i] in nums[i+1:]:
                index: int = nums[i+1:].index(num[i])
                return(i , index+i+1) 