class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return(False)
        else:
            x_str= str(x)
            return(x_str == x_str[::-1])