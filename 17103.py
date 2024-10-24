import sys

# def isPrime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# primeDict = {}

# for i in range(1, 1000001):
#     primeDict[i] = i if isPrime(i) else -1
        
# print("primeDict is ready")

# 에라토스테네스의 체

primeList = [1 for _ in range(1000001)]
primeList[1] = 0

# 2부터 시작해서, 그 수의 배수들을 모두 지우감.
# 이미 지워진 수면 넘어감.
# ex. 2의 배수 다 지우고
# 3의 배수 다 지우고...
# 그러다가 6에 도달하면, 6은 스킵하는 거(6은 이미 지워졌으니까)
# 그러면 이제 소수만 남는다고 함.
for i in range(2, 1000001):
    if primeList[i]:
        for j in range(i*2, 1000001, i):
            primeList[j] = 0

T = int(sys.stdin.readline().rstrip())
        
for i in range(T):
    input_number = int(sys.stdin.readline().rstrip())
    count = 0
    for j in range(input_number-1, input_number//2 - 1, -1):
        # if (isPrime(j)):
        # if (primeDict[j]) and (primeDict[j] > 0):
        if (primeList[j]) and (primeList[j] > 0):
            # if (isPrime(input_number-j)):
            # if (primeDict[input_number-j]) and (primeDict[input_number-j] > 0):
            if (primeList[input_number-j]) and (primeList[input_number-j] > 0):
                # print("goldbach partition number : ", j, input_number-j)
                count += 1
    print(count)