class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = {}

        def dfs(s1,s2):
            
            ans = 0
            
            if s1 >= len(text1) or s2 >= len(text2):
                return 0

            if (s1,s2) in dp:
                return dp[(s1,s2)]

            if text1[s1] == text2[s2]:
                ans += 1
                s1 += 1
                s2 += 1
                return ans + dfs(s1,s2)
            else:
                ans = max(dfs(s1+1, s2), dfs(s1, s2+1))
            
            dp[(s1,s2)] = ans

            return ans

        return dfs(0,0)