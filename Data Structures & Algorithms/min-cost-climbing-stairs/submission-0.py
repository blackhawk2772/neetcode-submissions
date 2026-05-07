class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # calculate min cost

        step1 = step2 = 0

        # step2, step1, n

        i = 0

        while i < len(cost):
            
            temp = cost[i] + min(step1,step2)
                 
            step2=step1
            step1=temp
            i+=1
            
        return min(step1,step2)