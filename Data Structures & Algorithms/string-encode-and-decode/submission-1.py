class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + ")" + string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        ptr = 0

        while ptr < len(s):
            length = ""

            while s[ptr] != ")":
                length += s[ptr]
                ptr += 1

            ptr += 1
            str_len = int(length)

            tempString = s[ptr:ptr + str_len]
            result.append(tempString)

            ptr += str_len

        return result