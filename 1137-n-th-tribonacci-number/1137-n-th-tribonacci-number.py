class Solution:
    def tribonacci(self, n: int) -> int:
        x: int = 0
        y: int = 1
        z: int = 1
        if n<2:
            return(n)
        elif n<3:
            return(n-1)
        else:
            for i in range(3,n+1):
                temp= x + y + z
                x= y
                y= z
                z= temp
            return(z)