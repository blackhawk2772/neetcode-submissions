class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        values = []
        res = []

        def dfs(i: int):

            if i >= len(nums):
                res.append(values.copy())
                return
            
            values.append(nums[i])
            dfs(i+1)
            
            values.pop()
            dfs(i+1)
        
        dfs(0)
        return res
