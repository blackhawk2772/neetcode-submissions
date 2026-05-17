class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def bSearch(left):
            l = 0
            r = len(nums)-1
            res = -1
            while l<=r:
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid -1
                else:
                    res = mid
                    if left:
                        r = mid - 1
                    else:
                        l = mid + 1
            return res
        
        a = bSearch(True)
        b = bSearch(False)
        return [a, b]
