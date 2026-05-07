class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for string in strs:
            basedict = {}

            for letter in string:
                if letter not in basedict:
                    basedict[letter] = 1
                else:
                    basedict[letter] += 1

            key = tuple(sorted(basedict.items()))

            if key not in groups:
                groups[key] = []

            groups[key].append(string)

        return list(groups.values())