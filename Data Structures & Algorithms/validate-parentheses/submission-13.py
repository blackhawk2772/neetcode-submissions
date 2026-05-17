class Solution:
    def isValid(self, s: str) -> bool:
        
        lookup = {}

        lookup[")"] = "("
        lookup["]"] = "["
        lookup["}"] = "{"

        stack = []

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if not stack or stack.pop() != lookup[c]:
                    return False
        
        return False if stack else True