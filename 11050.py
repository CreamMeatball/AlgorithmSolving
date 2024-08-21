N, K = map(int, input().split())

def combination(N, K):
    if K == 0 or N == K:
        return 1
    else:
        # 수학 공식. 이용해서 재귀로 풀 수 있음.
        return combination(N-1, K-1) + combination(N-1, K)
    
def combination2(N, K):
    if K == 0 or N == K:
        return 1
    else:
        return int(factorial(N) / (factorial(N-K) * factorial(K)))
        
        
def factorial(N):
    if N == 0:
        return 1
    number = 1
    for i in range(N):
        number *= (i+1)
    return number

print(combination(N, K))
# print(combination2(N, K))