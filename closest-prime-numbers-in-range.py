class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.getPrimes(left,right)
        
        minPair = 0
        size = len(primes)
        if size < 2:
            return [-1,-1]
        for i in range(size-1):
            if (primes[i+1] - primes[i]) < (primes[minPair+1] - primes[minPair]):
                minPair = i
        return [primes[minPair],primes[minPair+1]]



    def getPrimes(self,left,num):
        primes = [True for i in range(num+1)]
        primes[0] = primes[1] = False
        d = 2
        while d*d <= num:
            j = d*d
            if primes[j]:
                while j <= num:
                    primes[j] = False
                    j += d
            d += 1
        result = []

        for index,isPrime in enumerate(primes):
            if isPrime and index >= left:
                result.append(index)
        return result