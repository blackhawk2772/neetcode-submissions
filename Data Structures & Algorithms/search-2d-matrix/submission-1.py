class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right =  m * n - 1

        while left <= right:
        # 3x4 = 12 - 1 = 11
        # 11 // 2 = 5.5 -> 5.0
        # 5 // 3 =  1 -> we know its m = 1
        # 5 // 4 = 1 -> n = 1
        # 7 // 3 = 2
        # 7 // 4 = 1
            mid = (left + right) // 2
            i = mid // n
            j = mid % n 

            if matrix[i][j] == target: return True
            elif matrix[i][j] > target: right = mid-1
            else: left = mid+1

        return False