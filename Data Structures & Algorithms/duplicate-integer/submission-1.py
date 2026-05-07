class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        dicc = {}
        for i in range(len(nums)):
            if nums[i] not in dicc:
                 dicc[nums[i]] = 1
            else:
                result = True
                break


        return result
