class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i= len(nums1)
        while n>0 and m>0:
            if nums1[m-1]> nums2[n-1]:
                i-= 1
                m-= 1
                nums1[i]= nums1[m]
            else:
                i-= 1
                n-= 1
                nums1[i]= nums2[n]
        if n> 0:
            nums1[0:n] = nums2[0:n]