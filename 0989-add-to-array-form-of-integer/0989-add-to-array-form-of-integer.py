class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i= len(num)

        while i > 0 or k > 0 :
            if i > 0 and k > 0:
                k+= num[i-1]
                num[i-1]= k % 10
                k//= 10
                i-= 1
            elif k > 0:
                num.insert(0,k % 10)
                k//= 10
            else:
                break

        return num    
    
        