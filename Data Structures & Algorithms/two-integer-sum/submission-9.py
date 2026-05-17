class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        vals = {} # numb : index

        # nums[i] + nums[j] == target
        # target - nums[i] == nums[j]
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in vals:
                return [vals[diff],i]
            vals[nums[i]] = i
