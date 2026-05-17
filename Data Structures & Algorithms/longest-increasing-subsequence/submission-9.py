class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # [9,1,4,2,3,3,7,4, 8 ]

        n = len(nums)
        dp = [1] * n

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)