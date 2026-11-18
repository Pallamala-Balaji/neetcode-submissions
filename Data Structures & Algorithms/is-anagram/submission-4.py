class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h={}
        for i in s:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
        h1={}
        for i in t:
            if i not in h1:
                h1[i]=1
            else:
                h1[i]+=1
            
               
        return h==h1


        