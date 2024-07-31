# 조합 문제.
# combination 함수와 factorial 함수로 해결. 
# factorial 함수 작성 시 재귀형으로 쓰면 한계 초과로 에러남. 

testCaseNum = int(input())

N = []
M = []

for i in range(testCaseNum):
    n, m = map(int, input().split())
    N.append(n)
    M.append(m)
    
result = []

def combination(n, r):
    if n == r:
        return 1
    return int(factorial(n) / (factorial(r) * factorial(n-r)))
    
    
def factorial(n):
    if n == 1:
        return 1
    for i in range(1, n):
        n *= i
    return n

for i in range(testCaseNum):
    result.append(combination(M[i], N[i]))
    
for i in range(testCaseNum):
    print(result[i])
    