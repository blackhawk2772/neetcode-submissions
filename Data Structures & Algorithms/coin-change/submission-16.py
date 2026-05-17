class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}


        def dfs(value):

            if value == amount:
                return 0
            
            if value > amount:
                return amount+1
            
            if value in dp:
                return dp[value]

            res = amount+1

            for coin in coins:
                res = min(res, 1 + dfs(value+coin))
            
            dp[value] = res

            return res

        ans = dfs(0)

        return ans if ans <= amount else -1