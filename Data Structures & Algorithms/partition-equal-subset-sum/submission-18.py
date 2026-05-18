class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        if total % 2 != 0:
            return False

        dp = {}
        
        def dfs(i, amount):
            
            if amount * 2 == total:
                return True

            if i >= len(nums) or amount * 2 > total:
                return False
            
            if (i, amount) in dp:
                return dp[(i,amount)]
            
            take = dfs(i+1, amount + nums[i]) 
            skip = dfs(i + 1, amount)

            dp[(i,amount)] = take or skip

            return take or skip
    
        return dfs(0, 0)

             