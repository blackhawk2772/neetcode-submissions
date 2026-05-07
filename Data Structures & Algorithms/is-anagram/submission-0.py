class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sdic = {}
        tdic = {}

        for letter in s:
            if letter not in sdic:
                sdic[letter] = 1
            else:
                sdic[letter] += 1

        for letter in t:
            if letter not in tdic:
                tdic[letter] = 1
            else:
                tdic[letter] += 1

        if sdic == tdic:
            return True
        else:
            return False