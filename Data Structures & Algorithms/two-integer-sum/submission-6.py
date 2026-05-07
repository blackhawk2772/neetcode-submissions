class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # i + j = target
        # target - j = i
        # for

        prev = {}

        for i in range(len(nums)):
            diff =  target - nums[i]
            if diff in prev:
                return [prev[diff], i]
            else:
                prev[nums[i]] = i

