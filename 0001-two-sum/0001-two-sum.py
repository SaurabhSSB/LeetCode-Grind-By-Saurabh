class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        n=len(nums)
        mid=n//2
        for i in range(mid):
            if target-nums[i] in dict:
                return(i, dict[target- nums[i]])
            else:
                dict[nums[i]]= i
            a= n-i-1
            if target- nums[a]in dict:
                return(a, dict[target- nums[a]])
            else:
                dict[nums[a]]= a
            if (n/2!=0):
                if target- nums[mid] in dict:
                    return(mid,dict[target- nums[mid]])
