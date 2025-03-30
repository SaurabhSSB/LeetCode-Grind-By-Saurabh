class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        x: str = str(k)
        f= 0
        if len(num) >= len(x):
            size= len(x)
        else:
            size= len(num)
            li= list(map(int,list(str(x))))
            x= "".join(map(str,num))
            num=li

        for i in range(size):
        
            if num[-(i+1)] + int(x[-(i+1)]) > 9:
                
                if i+2 <= len(num):
                    j=i

                    while j+2 <= len(num) and num[-(j+2)]+ 1 > 9:
                        num[-(j+1) - 1]= (num[-(j+1)- 1] + 1) % 10
                        j+=1
                    
                    if j+2 <= len(num):    
                        num[-(j+1)- 1]+= 1

                    else:
                        num.insert(0,1)

                else:
                    num.insert(0,1)

            num[-(i+1)]= (num[-(i+1)] + int(x[-(i+1)])) % 10 

        return(num)