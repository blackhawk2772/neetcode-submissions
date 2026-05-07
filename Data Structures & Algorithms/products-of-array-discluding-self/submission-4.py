class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # array with nums
        # ex:   [1,2,4,6]
        # Out: [48,24,12,8]
        #
        # the idea would be to not repeat operations
        # 
        # bruteforcing it is O(n^2)
        #
        #

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]

        return output