class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = sorted(nums)
        current = 0
        max = 0
        
        for i in range(0, len(nums)):
            if nums[i]-nums[i-1] == 1 or i == 0:
                current += 1
                if current > max: max = current
            elif nums[i]-nums[i-1] == 0:
                continue
            else:
                current=1
        return max