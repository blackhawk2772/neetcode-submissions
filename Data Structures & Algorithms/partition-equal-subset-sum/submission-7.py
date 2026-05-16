class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2
        M = len(nums)

        dp = [[-1] * (target+1) for _ in range(M)]

        def dfs(i, count):
            
            if target - count == 0:
                return count
            
            if i >= M or target - count < 0:
                return 0
            
            if dp[i][count] != -1:
                return dp[i][count]

            dp[i][count] = max(dfs(i+1, count+nums[i]), dfs(i+1, count))

            return dp[i][count]
        
        if dfs(0, 0) - target == 0:
            return True
        else:
            return False