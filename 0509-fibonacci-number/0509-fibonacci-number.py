class Solution:
    def fib(self, n: int) -> int:
        x: int = 0
        y: int = 1

        if n <= 1:
            return(n)
        else:
            for i in range(2,n+1):
                z: int =x
                x= y
                y+= z
        return(y)