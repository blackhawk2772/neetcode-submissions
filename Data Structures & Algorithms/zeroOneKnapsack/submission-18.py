class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity

        nutsack = [[-1] * (M+1) for _ in range(N) ]
        
        def helper(i, cap):

            if i == len(profit):
                return 0
            
            if nutsack[i][cap] != -1:
                return nutsack[i][cap]
            
            nutsack[i][cap] = helper(i+1, cap)

            newCap = cap - weight[i]

            if newCap >= 0:

                res = profit[i] + helper(i+1, newCap)
                nutsack[i][cap] = max(res, nutsack[i][cap])

            return nutsack[i][cap]

        return helper(0, capacity)