class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets = []
        res = []

        def helper(i: int):

            if sum(subsets) == target:
                res.append(subsets.copy())     
                return
            elif i >= len(nums) or sum(subsets) > target:
                return

            if sum(subsets) < target and i<len(nums):
                subsets.append(nums[i])
                helper(i)
                subsets.pop()
            
            helper(i+1)

        helper(0)

        return res