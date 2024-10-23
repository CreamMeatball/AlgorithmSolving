def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# primeList = [i for i in range(2, 123456*2+1) if isPrime(i)]
primeDict = {}
for i in range(2, 123456*2+1):
    primeDict[i] = i if isPrime(i) else -1

while(True):
    N = int(input())
    if N == 0:
        break
    numberOfPrime = 0
    # for i in range(N+1, N*2+1):
    #     if isPrime(i):
    #         numberOfPrime += 1
    for i in range(N+1, N*2+1):
        if primeDict[i] != -1:
            numberOfPrime += 1
    
    print(numberOfPrime)