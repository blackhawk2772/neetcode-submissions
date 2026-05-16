class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        ds1 = defaultdict(int)
        ds2 = defaultdict(int)
        winSize= len(s1)

        for c in s1:
            ds1[c] += 1
        
        def valid(ds1,ds2):
            for key in ds1:
                if ds1[key] != ds2[key]:
                    return False
            return True

        l = 0
        r = winSize-1

        for i in range(winSize):
            ds2[s2[i]]+=1

        #  s1 = "abc", s2 = "lecabee"
        
        while r < len(s2):            
            if valid(ds1,ds2):
                return True

            ds2[s2[l]] -= 1
            l += 1
            r += 1
            
            if r < len(s2):
                ds2[s2[r]] += 1
            
        return False
