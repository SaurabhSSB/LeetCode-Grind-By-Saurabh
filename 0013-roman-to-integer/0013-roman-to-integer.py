class Solution:
    def romanToInt(self, s: str) -> int:
        a= len(s)
        b=0
        for i in range(a):
            match(s[i]):
                case "M":
                    b+= 1000
                case "D":
                    b+= 500
                case "C":
                    if(i== a-1 or (s[i+1]!= "M" and s[i+1]!= "D")):
                        b+= 100
                    else:
                        b-=100
                case "L":
                    b+= 50
                case "X":
                    if(i== a-1 or (s[i+1]!= "L" and s[i+1]!= "C")):
                        b+= 10
                    else:
                        b-=10
                case "V":
                    b+= 5
                case "I":
                    if(i== a-1 or (s[i+1]!= "V" and s[i+1]!= "X")):
                        b+= 1
                    else:
                        b-=1
        return(b)