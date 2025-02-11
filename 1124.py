# 시간 초과 문제 때문에 PyPy3로 제출 필요.

A, B = map(int, input().split())

testPrint = False

def primeFactorization(number):
    print(f"-- primeFactorization() init") if testPrint else None
    primeList = []
    global EratosPrimeList
    # for i in range(2, number + 1):
    #     # number ** (0.5) + 1 로 하면 안됨.
    #     # 예를 들어 number = 3인 경우 root(3) + 1 = 2.732... 이므로 2까지만 loop를 돌아서 문제가 발생함.
    #     if number <= 1: # 효율성을 위해 여기서 조건부 break
    #         break
    #     while(number % i == 0):
    #         primeList.append(i)
    #         number //= i
    #         print(f"divide by {i}, number: {number}") if testPrint else None  
    divisor = 2
    while number > 1:
        if EratosPrimeList[divisor] and number % divisor == 0:
            primeList.append(divisor)
            number //= divisor
            print(f"divide by {divisor}, number: {number}") if testPrint else None
        else:
            divisor += 1
    print(f"-- primeFactorization() end") if testPrint else None
        
    return primeList
    
def isUnderPrime(A, B):
    underPrimeList = []
    global EratosPrimeList
    
    for i in range(A, B + 1):
        if EratosPrimeList[i]: # 시간 초과 문제 때문에 무조건 해야하는 조건문.
            continue
        print(f"[ i: {i} ]") if testPrint else None
        primeList = primeFactorization(i)
        print(f"{i}'s primeList : {primeList}") if testPrint else None
        if EratosPrimeList[len(primeList)]:
            print(f"★ {i} is underPrime") if testPrint else None
            underPrimeList.append(i)
        else:
            print(f"{i} is not underPrime") if testPrint else None
    print(f"underPrimeList: {underPrimeList}") if testPrint else None
    
    return len(underPrimeList)

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def isPrimeEratos(number):
    # 에라토스테네스의 체
    # 시간이 더 빠른 대신 메모리가 더 많이 들음.
    if number <= 1:
        return False
    prime = [False, False] + [True] * (number - 1)
    for i in range(2, int(number ** 0.5) + 1):
        if prime[i]:
            j = 2
            while i * j <= number:
                prime[i * j] = False
                j += 1
    return prime

EratosPrimeList = isPrimeEratos(B)
print(isUnderPrime(A, B))