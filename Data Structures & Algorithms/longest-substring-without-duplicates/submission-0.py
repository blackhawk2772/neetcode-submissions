class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer=0
        current = set()        
        maximum=0
        i=0
        j=0
        if len(s) == 0:  # FIX: Move empty check outside loop
            return 0
        while j<len(s):
            if s[j] not in current:  # FIX: Check if s[j] is in window, not just equal to s[i]
                answer+=1
                current.add(s[j])
                if answer > maximum:
                    maximum = answer
                j+=1
            else:
                # FIX: Remove s[i] only if it exists, and continue until s[j] is no longer in set
                current.remove(s[i])
                i+=1
                answer-=1
        return maximum