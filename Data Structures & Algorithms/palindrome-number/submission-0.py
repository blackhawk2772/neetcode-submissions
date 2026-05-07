class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        # 7 / 2 = 3,5
        # 121 / 2 = 60,5
        # 60 / 2 = 30 / 2 = 15 / 2 = 
        # 66 / 2 = 33 / 2 = 16,5
        # 11 / 2 = 5,5


        i = 0
        s = str(x)
        j = len(s)-1
        while i <= j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True