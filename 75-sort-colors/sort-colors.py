class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left= 0
        right= len(nums)- 1
        current= 0
        while(current <= right):
            if nums[current] == 1:
                current+= 1
                continue
            elif nums[current] == 0:
                nums[current], nums[left]= nums[left], nums[current]
                current+= 1
                left+= 1
            else:
                nums[current], nums[right]= nums[right], nums[current]
                right-= 1
        