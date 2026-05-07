class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prev = {} # store as n : i

        #
        # nums = [3,4,5,6], target = 7
        # n + n2 = target
        # target - n = neededNum
        # 
        
        for i,n in enumerate(nums):
            diff = target - n
            
            if  diff in prev:
                return [prev[diff], i]
            
            prev[n] = i

        return 

