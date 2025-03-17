class Solution:
    def isPalindrome(self, x: int) -> bool:
        isPalin= 1
        x_str: str = str(x)
        for i in range(len(x_str)//2):
            if x_str[i] != x_str[-(1+i)]:
                isPalin= 0
        
        if isPalin == 1:
            return(True)
        else: 
            return(False)