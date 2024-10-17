import sys

T = int(sys.stdin.readline().rstrip())

# 최소공배수 : '두 수의 곱 / 최대공약수'로 구할 수 있다고 함(유클리드 호제법)

def gcd(a, b): # greatest common divisior
    while b:
        a, b = b, a % b
    return a

def lcm(a, b): # least common multiple
    return a * b // gcd(a, b)

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(lcm(A, B))