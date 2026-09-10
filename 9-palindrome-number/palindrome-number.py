class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y= str(x)
        n= len(y)
        for i in range(n//2):
            if y[i] != y[n-i-1]:
                return False
        return True        