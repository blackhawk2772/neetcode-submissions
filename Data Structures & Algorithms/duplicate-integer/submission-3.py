class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev =  set()

        for i in range(len(nums)):
            if nums[i] in prev: return True
            prev.add(nums[i])
        return False
