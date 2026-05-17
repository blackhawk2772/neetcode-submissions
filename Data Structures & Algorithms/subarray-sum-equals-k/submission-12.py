class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
         
        prefixSum = defaultdict(int)
        curr = 0
        total = 0
        for num in nums:
            # add prefix sum as a +1 frequency
            prefixSum[curr] += 1
            # maintain running count
            curr += num
            # if curr + ? = k, then we can find ? with k - curr
            # if ? exists as a previous prefix sum, we can add the frequency of # of prefix subarrays
            total += prefixSum[curr - k]
        return total