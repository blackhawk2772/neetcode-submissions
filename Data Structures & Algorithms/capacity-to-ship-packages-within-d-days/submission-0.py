class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # weights = [1,2,3,4,5,6,7,8,9,10], days = 5

        #  minimum = max(weights) ; maximum = sum(weights)

        # 10 .. 55
        
        def canShip(weights: List[int], days: int, capacity: int):
            current = 0
            ndays = 1
            for i in range(len(weights)):
                if current + weights[i] > capacity:
                    current = weights[i]
                    ndays += 1
                else:
                    current += weights[i]

            if ndays <= days:
                return True
            else:
                return False

        l = max(weights)
        r = sum(weights)

        while l < r:

            mid = (l + r) // 2
            if canShip(weights, days, mid):
                r = mid
            else:
                l = mid+1

        return l