import random

# N 이 분해합(결과값)
N = int(input())

def decompositionSum(M):
    sum = int(M)
    M = str(M)
    for i in range(len(M)):
        sum += int(M[i])
    # print(M, "'s decomSum is ", sum)
    return sum

M = list(range(1, N+1))
result = []

for i in M:
    if decompositionSum(i) == N:
        result.append(i)
        
# print(result)
print(min(result)) if result else print(0)