class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        lista = [[] for _ in range(len(nums) + 1)]
        output = []

        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1

        for elem in dictionary:
            lista[dictionary[elem]].append(elem)

        for i in range(len(lista) - 1, 0, -1):
            for elem in lista[i]:
                output.append(elem)
                if len(output) == k:
                    return output