class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        vals = []
        nums = sorted(nums)

        def dfs(i: int):

            if i >= len(nums):
                res.append(vals.copy())
                return
            
            vals.append(nums[i])
            dfs(i+1)
            
            vals.pop()
            
            jump = i+1
            
            while jump < len(nums) and nums[jump] == nums[i]:
                jump +=1
            dfs(jump)

        dfs(0)

        return res