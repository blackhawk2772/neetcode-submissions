class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        
        self.dfs(nums,[])

        return self.res

    def dfs(self, nums, cur):

        if not nums:
            self.res.append(cur.copy())
            return

        for i in range(len(nums)):
            cur.append(nums[i])
            self.dfs(nums[:i] + nums[i+1:], cur)
            cur.pop()
                    
        return