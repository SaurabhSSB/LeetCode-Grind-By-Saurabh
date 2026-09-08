class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rolling_sum= nums[0]
        max_sum= nums[0]
        for i in range(1, len(nums)):
            if rolling_sum > 0:
                rolling_sum+= nums[i]
            else:
                rolling_sum= nums[i]
            if max_sum < rolling_sum:
                max_sum= rolling_sum

        return(max_sum)