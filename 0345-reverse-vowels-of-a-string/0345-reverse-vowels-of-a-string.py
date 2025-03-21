class Solution:
    def reverseVowels(self, s: str) -> str:
        a= list(s)
        vowels= "aeiouAEIOU"
        start= 0
        end= len(s) - 1
        while(start < end):
            if a[start] not in vowels:
                start+= 1
            elif a[end] not in vowels:
                end-= 1
            else:
                a[start] , a[end] = a[end] , a[start]
                start+= 1
                end-= 1

        return ("".join(a))