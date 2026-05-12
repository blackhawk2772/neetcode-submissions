class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        M = len(nums)
        N = target
        offset = sum(nums)
        cache = [[-1] * (2 * offset + 1) for _ in range(M)]
        
        def solver(i, cur):
            if i == M and cur == 0:
                return 1
            
            if abs(cur) > offset or i == M:
                return 0 

            if cache[i][cur+offset] != -1:
                return cache[i][cur+offset]

            cache[i][cur+offset] = solver(i+1, cur + nums[i]) + solver(i+1, cur - nums[i])
            return cache[i][cur+offset]

        return solver(0, target)