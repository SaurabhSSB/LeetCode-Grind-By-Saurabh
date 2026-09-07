class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last= len(nums)- 1
        for i in range(last, 0, -1):
            if nums[i] > nums[i-1]:
                pivot= i- 1
                break
        else:
            pivot= 0
        for i in range(last, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot]= nums[pivot], nums[i]
                pivot+= 1
                break
        left= pivot
        right= last
        while(left<right):
            nums[left], nums[right]= nums[right], nums[left]
            left+= 1
            right-= 1