class Solution:
    def isValid(self, s: str) -> bool:
        
        mirror = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

        stack = []

        for letter in s:
            if letter in "({[":
                stack.append(letter)
            else :
                if not stack or stack[-1] != mirror[letter]:
                    return False
                stack.pop()
        
        return True if not stack else False

            