class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h={}
        for i in nums:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1

        for i in h:
            if h[i]>=2:
                return True
        return False


        