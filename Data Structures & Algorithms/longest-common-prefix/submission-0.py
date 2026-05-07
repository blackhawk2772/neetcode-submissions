class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            current = strs[0][i]
            
            for text in strs:
                if (len(text)-1 < i )or text[i] != current:
                    return res
            res += current

        return res