class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        rob1,rob2 = 0,0
        
        # rob2, rob1, n, n+1

        for i in range(len(nums)-1):

            temp = max(rob2 + nums[i], rob1)
            
            rob2 = rob1
            rob1 = temp

        a = rob1
        rob1,rob2 = 0,0

        for i in range(1,len(nums)):

            temp = max(rob2 + nums[i], rob1)
            
            rob2 = rob1
            rob1 = temp

        return max(a,rob1)
