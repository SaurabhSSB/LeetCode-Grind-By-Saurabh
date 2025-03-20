class Solution:
    def isValid(self, s: str) -> bool:
        b=-1
        a=[]
        x={'(':1,'{':2,'[':3,']':6,"}":4,")":2}
        for i in s:
            if (i=="(" or i=="{" or i=="["):
                a.append(x[i])
                b=b+1
            elif(b>-1 and (i==")" or i=="}" or i=="]")):
                if a[b]== x[i]/2:
                    a.pop(b)
                    b=b-1
                else:
                    return(False)
            else:
                return(False)
        if(b== -1):
            return(True)
        else:
            return(False)
