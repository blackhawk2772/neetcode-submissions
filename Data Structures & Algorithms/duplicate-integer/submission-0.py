class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        dicc = {}
        for i in range(len(nums)):
            if nums[i] not in dicc:
                 dicc[nums[i]] = 1
            else:
                dicc[nums[i]] +=1

        for key in dicc:
            if dicc[key] > 1:
                result=True
        return result
