class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        p = 2

        for i in range(2,int(pow(n,0.5))+1):
            if isPrime[i]:
                for j in range(i*i,n,i):
                    isPrime[j] = False
                    p += 1
        primes = 0

        for i in range(2,n):
            primes += int(isPrime[i])

        return primes