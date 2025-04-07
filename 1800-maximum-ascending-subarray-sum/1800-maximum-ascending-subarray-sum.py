class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        num: List[int] = [nums[0]]
        elsum: List[int] = []

        for i in range(len(nums)):
            if nums[i] > num[-1]:
                num.append(nums[i])
            else:
                elsum.append(sum(num))
                num= [nums[i]]
        elsum.append(sum(num))

        return(max(elsum))