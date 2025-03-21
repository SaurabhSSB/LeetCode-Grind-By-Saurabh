class Solution:
    def reverseVowels(self, s: str) -> str:
        a= list(s) 
        dvi= {}

        for i,ch in enumerate(s):
            if ch.lower() in "aeiou":
                dvi[i]= ch

        dvik= list(dvi.keys())

        for reverse in range(len(dvik)//2):
            a[dvik[reverse]] , a[dvik[-(reverse+1)]] = a[dvik[-(reverse+1)]] , a[dvik[reverse]]

        return ("".join(a))