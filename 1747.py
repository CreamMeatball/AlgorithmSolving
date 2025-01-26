N = int(input())

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def Palindrome(n):
    return str(n) == str(n)[::-1]

for i in range(N, 1003002): # N 범위는 1000000까지지만 1000000 이상의 가장 작은 소수까지 해야 함.
    if isPrime(i) and Palindrome(i):
        print(i)
        break