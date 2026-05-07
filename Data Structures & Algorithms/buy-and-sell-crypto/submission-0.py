class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # iterarate through array with i index
        # subtract j - i number to get the profit, and store it in output variable
        # keep on cycling until finished and updating the output with the max value found until that moment

        profit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if (prices[j]-prices[i]) > profit:
                    profit = prices[j]-prices[i]

        return profit