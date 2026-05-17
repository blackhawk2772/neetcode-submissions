from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1

        prefix = 0
        ans = 0

        for num in nums:
            prefix += num

            diff = prefix - k
            ans += count[diff]

            count[prefix] += 1

        return ans