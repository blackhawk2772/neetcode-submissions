from heapq import heappush, heappop, heapify 
class KthLargest:
        
    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        self.nums = nums
        self.k = k
        if nums:
            self.max = nums[0]
        else: 
            self.max= None
        
    def add(self, val: int) -> int:
        heappush(self.nums,val)
        # [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
        # 3 kth element; heapify -> [2,4,5,8] (aprox) 
        #  push 3 -> [2, 3, 4, 5, 8]
        #   len = 5 -> [3, 4, 5, 8], len=4 [4, 5, 8] pop [5,8] return 4
        # push 5 -> len = 3 we good pop [5, 8] return 5
        # push 10 -> [8, 10] return 5
        # push 9 -> [9,10] return 8
        # push 4 -> [9,10] return 4
        while len(self.nums) > self.k:
            heappop(self.nums)

        return self.nums[0]
