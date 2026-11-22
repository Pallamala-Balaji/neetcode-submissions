class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=""
        for i in s:
            if i.isalnum():
                r=r+i.lower()
        
        l=list(r)
        i=0
        j=len(l)-1
        while i<j:
            if l[i]!=l[j]:
                return False
            i+=1
            j-=1
        return True
                

        