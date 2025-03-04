N = int(input())

def makePrimeList(n):
    # using Eratosthenes' sieve
    sieve = [True] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i] == True]

# print(makePrimeList(N))

start, end = 0, 0
count = 0

primeList = makePrimeList(N)
sumOfPrimes = 0

while start <= end:
    if sumOfPrimes == N:
        count += 1
        sumOfPrimes -= primeList[start]
        start += 1
    elif sumOfPrimes < N:
        if end == len(primeList):
            break
        sumOfPrimes += primeList[end]
        end += 1
    else:
        sumOfPrimes -= primeList[start]
        start += 1
        
print(count)