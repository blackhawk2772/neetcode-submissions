class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # [9,1,4,2,3,3,7,4, 8 ]

        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]

            best = 1  # nums[i] itself

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))

            dp[i] = best
            return best

        ans = 0
        for i in range(len(nums)):
            ans = max(ans, dfs(i))

        return ans