class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        r = len(s)-1
        # 5 -> 2 + 1 = 3
        # l0,r4; l1,r3; l2,r2
        for l in range((len(s)//2)):
            s[l], s[r] = s[r], s[l]
            r -= 1