class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        a = 0
        b = len(heights)-1
        maximum = 0

        while a < b:
            minimum = min(heights[a], heights[b])
            dist = b - a
            if (minimum * dist) > maximum:
                maximum = dist * minimum
            if heights[a] < heights[b]:
                a += 1
            else:
                b -= 1

        return maximum