class Solution:
    def rob(self, nums: List[int]) -> int:
                
        roba,robb = 0,0

        #   [1,2,3,1]
        #   roba, robb, nums  
        
        for n in nums:
            temp=max(roba+n,robb)
            roba = robb
            robb=temp
        
        return robb