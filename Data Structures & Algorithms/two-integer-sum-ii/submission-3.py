class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #numbers growing order
        # only one valid solution
        #given a list, find two values that when summed up, they equal a target values

        #numbers = [1,2,3,4], target = 3 ->  

        ptr_a = 0
        ptr_b = len(numbers)-1
        
        for i in range(len(numbers)):
            if numbers[ptr_a] + numbers[ptr_b] == target:
                return [ptr_a+1, ptr_b+1]
            else:
                if numbers[ptr_a] +  numbers[ptr_b] > target:
                    ptr_b -= 1
                elif numbers[ptr_a] +  numbers[ptr_b] < target:
                    ptr_a += 1
                
        return [ptr_a+1,  ptr_b+1]
