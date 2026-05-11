class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {}
        colors[0] = 0
        colors[1] = 0
        colors[2] = 0
    
        for i in range(len(nums)):
            colors[nums[i]] += 1

        for i in range(len(nums)):
            if i < colors[0]:
                nums[i] = 0
            elif i - colors[0] < colors[1]:
                nums[i] = 1
            else:
                nums[i] = 2