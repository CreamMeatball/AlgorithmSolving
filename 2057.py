import sys
import math

N = int(input())

def factorial(n):
    sum_ = 1
    while n > 0:
        sum_ *= n
        n -= 1
    return sum_

# 0 1 2 3 4  5   6   7
# 1 1 2 6 24 120 720 5040 ...

# 가능한 수가
# 1, 2, 3, 4, 6, 7, 8, 9, 10, 24, 25, ...

if N == 0: # 아래 알고리즘 상으론 0을 못 걸러내므로.
    print("NO")
    sys.exit()

# for i in range(math.ceil(math.sqrt(N)), -1, -1):
range_ = min(20, math.ceil(math.sqrt(N)))
# 19! < 10**18 < 20! 이라서
# 문제의 조건(10**18) 내에서 작동하려면 어차피 19! 까지밖에 필요 없음.
for i in range(range_, -1, -1):
    factorial_val = factorial(i)
    # print(i, N)
    if factorial_val <= N:
        N = N - factorial_val
        continue
    
if N == 0:
    print("YES")
else:
    print("NO")