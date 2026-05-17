class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
         
        prefixSum = [0] * len(nums)
        hashmap = defaultdict(int)

        ans = 0

        for i in range(len(nums)):
            if i == 0:
                prefixSum[i] = nums[i]
            else:
                prefixSum[i] = nums[i] + prefixSum[i - 1]

            # prefixSum[i] - prefixSum[j] = k
            # prefixSum[j] = prefixSum[i] - k

            diff = prefixSum[i] - k 

            if diff == 0:
                ans += 1

            if diff in hashmap:
                ans += hashmap[diff]

            hashmap[prefixSum[i]] += 1
        
        return ans