from collections import defaultdict
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}

        def dfs(i, value):
            if value == amount:
                return 0

            if value > amount or i >= len(coins):
                return -1
            
            if (i, value) in dp:
                return dp[(i, value)]
            
            add = dfs(i, value + coins[i])
            skip = dfs(i + 1, value)

            # If we used coins[i], count that coin
            if add != -1:
                add = 1 + add

            # Choose the smaller valid answer
            if add == -1:
                dp[(i, value)] = skip
            elif skip == -1:
                dp[(i, value)] = add
            else:
                dp[(i, value)] = min(add, skip)

            return dp[(i, value)]
        
        return dfs(0, 0)