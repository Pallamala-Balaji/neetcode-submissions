class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maximum=float("-inf")
        while (i<j):
            area=(j-i)*min(heights[i],heights[j])
            maximum=max(maximum,area)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maximum

        