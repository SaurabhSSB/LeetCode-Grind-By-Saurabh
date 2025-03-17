class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        b=""
        a=0
        for i in (strs[0]):
            for j in strs[1:]:
                if(a== len(j)):
                    return(b)
                if (i!= j[a]):
                    return(b)
            b+=i
            a+=1
        return(b)