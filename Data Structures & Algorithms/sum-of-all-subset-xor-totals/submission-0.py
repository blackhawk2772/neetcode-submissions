class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def helper(i: int, vals: int):
            
            if i >= len(nums):
                return vals

            return helper(i+1, vals ^ nums[i]) + helper(i+1,vals)
        
        return helper(0,0)