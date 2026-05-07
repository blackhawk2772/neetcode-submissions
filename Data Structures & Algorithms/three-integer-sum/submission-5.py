class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []

        for i, n in enumerate(nums):
            # FIX: Skip duplicate values for i to avoid redundant triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i+1
            k = len(nums)-1
            # nums = [-4 , -1, -1, 0, 1, 2]
            while j < k:
                if nums[j] + nums[k] == -n:
                    output.append([n, nums[j], nums[k]])
                    # FIX: Skip duplicates for j and k after finding a match
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                    j += 1
                elif nums[j] + nums[k] > -n:
                    k -= 1
                elif nums[j] + nums[k] < -n:
                    j += 1
        return output


