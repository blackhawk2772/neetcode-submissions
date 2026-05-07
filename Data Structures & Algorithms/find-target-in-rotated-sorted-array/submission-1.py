class Solution:
    def search(self, nums: List[int], target: int) -> int:
         
        left = 0
        right = len(nums)-1

        while left <= right:
            
            mid = (left + right) // 2

            if nums[mid]== target:
                return mid
            
            # on right side
            if nums[mid] >=  nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            # on left side
            else: 
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            # [2,3,4,5,6,7,0,1], target = 3  
        
        return -1