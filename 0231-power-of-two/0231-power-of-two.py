class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n<1):
            return False
        while(n>1):
            if n%2 != 0:
                return False
            n/= 2
        return True
