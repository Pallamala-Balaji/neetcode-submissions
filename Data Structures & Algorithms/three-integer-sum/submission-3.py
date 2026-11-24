class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        h=set()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while(j<k):
                total=nums[i]+nums[j]+nums[k]
                if total==0:
                    a=(nums[i],nums[j],nums[k])
                    h.add(a)
                    j+=1
                    k-=1
                elif total>0:
                    k-=1
                else:
                    j+=1
        return [list(x) for x in h]
        
        
        