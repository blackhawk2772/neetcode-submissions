class Solution:
    def tribonacci(self, n: int) -> int:
        n1,n2,n3 = 0,0,1

        for i in range(n):
            temp = n1+n2+n3
            n3=n2
            n2=n1
            n1=temp

        return n1