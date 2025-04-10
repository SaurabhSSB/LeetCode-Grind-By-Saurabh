class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        start= 0
        end= len(nums)-1
        mid= len(nums)//2
        find= []
        
        while(start <= end):
            if nums[mid] == target:
                find.append(mid)
                
                while mid+1 < len(nums) and nums[mid+1] == target:
                    find.append(mid+1)
                    mid+= 1

                while mid-1 >= 0 and nums[mid-1] == target:
                    find.insert(0, mid-1)
                    mid-= 1
                
                if len(find) > 1:
                    return [find[0], find[-1]]
                elif len(find) == 1:
                    return [find[0],find[0]]

            elif nums[mid] < target:
                start= mid+1
            else:
                end= mid-1
                
            mid= start + (end-start)//2

        return [-1,-1]