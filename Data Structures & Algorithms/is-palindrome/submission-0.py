class Solution:
    def isPalindrome(self, s: str) -> bool:

        palin = "".join(char.lower() for char in s if char.isalnum())
        length = len(palin)
        for i in range(length):
            if i >= (length-i-1):
                return True
            if palin[i] != palin[length-i-1]:
                return False

        return True