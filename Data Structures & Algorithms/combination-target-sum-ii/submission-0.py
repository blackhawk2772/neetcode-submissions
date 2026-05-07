class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        vals = []
        res = []
        candidates = sorted(candidates)

        def helper(i: int):

            if sum(vals) == target:
                res.append(vals.copy())
                return
            
            if sum(vals) > target or i >= len(candidates) :
                return
                        
            vals.append(candidates[i])
            helper(i+1)
            vals.pop()


            jump = i + 1
            while jump < len(candidates) and candidates[jump] == candidates[i]:
                jump +=1

            helper(jump)

        helper(0)

        return res