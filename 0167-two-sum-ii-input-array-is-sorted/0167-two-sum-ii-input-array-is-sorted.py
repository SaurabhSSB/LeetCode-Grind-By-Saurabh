class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target - numbers[i] in numbers[i+1:]:
                return(i+1, numbers[i+1:].index(target - numbers[i])+1+i+1)
            if target - numbers[-(i+1)] in numbers[:len(numbers)-(i+1)]:
                return(numbers[:len(numbers)-(i+1)].index(target - numbers[-(i+1)])+1,len(numbers)-(i+1) +1)
        