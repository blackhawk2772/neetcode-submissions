class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        M = len(strs)
        N = m+n

        nutsack = {}

        def solver(i, a, b):
            
            if a < 0 or b < 0 or i >= len(strs):
                return 0
            
            if nutsack.get((i,a,b),-1) != -1:
                return nutsack[i,a,b]
            
            skip = solver(i+1, a, b)
            
            zeros = 0
            ones = 0

            for letter in strs[i]:
                if letter == "0":
                    zeros += 1
                elif letter == "1":
                    ones +=1

            if zeros <= a and ones <= b:
                take = 1 + solver(i+1, a - zeros, b - ones)
            else:
                take = 0
            
            nutsack[(i,a,b)] = max(skip, take)

            return nutsack[(i,a,b)]

        return solver(0, m , n)