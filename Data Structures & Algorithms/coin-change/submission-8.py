from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}

        def dfs(i, value):
            if value == amount:
                return 0
            
            if value > amount or i >= len(coins):
                return amount+1
            
            if (i, value) in dp:
                return dp[(i, value)]
            
            add = 1 + dfs(i, value + coins[i])
            skip = dfs(i + 1, value)

            dp[(i, value)] = min(add, skip)

            return dp[(i, value)]
        
        ans = dfs(0, 0)
        return ans if ans <= amount else -1