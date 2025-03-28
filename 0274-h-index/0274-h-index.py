class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) < 1:
            if citation[0] < 1:
                return(0)
            else:
                return(1)
        
        else:
            li_1= citations
            li_1.sort(reverse= True)
            
            for i in range(1,len(li_1)+1):
                if i > li_1[i-1]:
                    return(i-1)
            return len(citations)