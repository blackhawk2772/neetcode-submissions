class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        hs = defaultdict(int)
        ht = defaultdict(int)
        ss = ""
        minSS = s

        # we check if we good
        def valid(hs, ht):
            for key in ht:
                if hs[key] < ht[key]:
                    return False
            return True

        for c in t:
            ht[c] += 1
        
        l,r = 0, 0
        found = False
        while r < len(s):
            ss += s[r]
            hs[s[r]] += 1
            r +=1

            while valid(hs,ht):
                found = True
                if len(ss)< len(minSS):
                    minSS = ss
                hs[s[l]] -=1
                ss = ss[1:]
                l += 1
        if found: return minSS
        else: return ""