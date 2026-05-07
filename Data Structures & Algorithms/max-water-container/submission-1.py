class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        i=0
        j = len(heights)-1
        while i<j:
        # min(a.height + b.height) multiply x distance -> b.index - a.index
            result = min(heights[i], heights[j])*(j-i)
                                        # 1 * 1-0-1 
            if result > maximum:
                maximum = result
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return maximum