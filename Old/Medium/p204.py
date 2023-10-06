class Solution:
    def countPrimes(self, n: int) -> int:
        a=[0]*n
        for i in range(2,n):
            if a[i]==0:
                for j in range(i*i,n,i):
                    a[j]=1
        return a[2:].count(0)