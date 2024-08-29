numberOfDivisor = int(input())

divisors = list(map(int, input().split()))
divisors.sort()

if numberOfDivisor%2 == 0:
    multiply = divisors[numberOfDivisor//2-1] * divisors[numberOfDivisor//2]
    print(multiply)
elif numberOfDivisor%2 == 1:
    multiply = divisors[numberOfDivisor//2] ** 2
    print(multiply)