class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = {}


        def dfs(i, value):
            
            if value == amount:
                return 1

            if value > amount or i>= len(coins):
                return 0
            
            if (i,value) in dp:
                return dp[(i, value)]

            ans = 0

            add = dfs(i, value+coins[i])

            skip = dfs(i+1, value)
            
            dp[(i,value)] = add+skip

            return dp[(i,value)]
        
        return dfs(0, 0)